from pathlib import Path

import pandas as pd
import pytest

from services.securities.parser import parse_html_to_df, validate_and_clean

FIXTURES = Path(__file__).parent / "fixtures"

EN_FIXTURE = (FIXTURES / "sample_set_response_en.html").read_text(encoding="utf-8")
TH_FIXTURE = (FIXTURES / "sample_set_response_th.html").read_text(encoding="utf-8")

EXPECTED_COLUMNS = ["symbol", "name", "market", "industry", "sector", "address", "zip", "tel", "fax", "web"]


# ── parse_html_to_df ─────────────────────────────────────────────────────────

def test_parse_en_fixture_returns_right():
    result = parse_html_to_df(EN_FIXTURE)
    assert result.is_right()


def test_parse_th_fixture_returns_right():
    result = parse_html_to_df(TH_FIXTURE)
    assert result.is_right()


def test_parse_en_column_names():
    df = parse_html_to_df(EN_FIXTURE).value
    assert list(df.columns) == EXPECTED_COLUMNS


def test_parse_th_column_names():
    df = parse_html_to_df(TH_FIXTURE).value
    assert list(df.columns) == EXPECTED_COLUMNS


def test_parse_en_row_count():
    # fixture has 5 data rows (after dropping 2 header rows)
    df = parse_html_to_df(EN_FIXTURE).value
    assert len(df) == 5


def test_parse_th_row_count():
    df = parse_html_to_df(TH_FIXTURE).value
    assert len(df) == 5


def test_parse_en_first_symbol():
    df = parse_html_to_df(EN_FIXTURE).value
    assert df.iloc[0]["symbol"] == "2S"


def test_parse_en_market_values():
    df = parse_html_to_df(EN_FIXTURE).value
    assert set(df["market"].unique()).issubset({"SET", "mai"})


def test_parse_en_both_markets_present():
    df = parse_html_to_df(EN_FIXTURE).value
    assert "SET" in df["market"].values
    assert "mai" in df["market"].values


def test_parse_no_table_returns_left():
    result = parse_html_to_df("<html><body>no table here</body></html>")
    assert result.is_left()
    assert result.monoid[0]  # non-empty error message


def test_parse_wrong_column_count_returns_left():
    html = "<table><tr><td>A</td><td>B</td></tr><tr><td>x</td><td>y</td></tr></table>"
    result = parse_html_to_df(html)
    assert result.is_left()
    assert "column count" in result.monoid[0]


def test_parse_empty_string_returns_left():
    result = parse_html_to_df("")
    assert result.is_left()


# ── validate_and_clean ───────────────────────────────────────────────────────

def _make_df(n: int = 1, **overrides) -> pd.DataFrame:
    """Build a minimal DataFrame with all required columns, n rows each."""
    base = {col: ["val"] * n for col in EXPECTED_COLUMNS}
    base["symbol"] = ["SYM"] * n
    base.update(overrides)
    return pd.DataFrame(base)


def test_validate_strips_whitespace():
    df = _make_df(symbol=["  PTT  "], name=["  PTT Company  "])
    result = validate_and_clean(df)
    assert result.iloc[0]["symbol"] == "PTT"
    assert result.iloc[0]["name"] == "PTT Company"


def test_validate_drops_null_symbols():
    df = _make_df(n=3, symbol=["PTT", None, "SCB"])
    result = validate_and_clean(df)
    assert len(result) == 2
    assert list(result["symbol"]) == ["PTT", "SCB"]


def test_validate_drops_empty_string_symbols():
    df = _make_df(n=3, symbol=["PTT", "", "SCB"])
    result = validate_and_clean(df)
    assert len(result) == 2
    assert list(result["symbol"]) == ["PTT", "SCB"]


def test_validate_raises_on_missing_symbol_column():
    df = pd.DataFrame({"name": ["X"], "market": ["SET"]})
    with pytest.raises(ValueError, match="symbol"):
        validate_and_clean(df)


def test_validate_resets_index():
    df = _make_df(n=3, symbol=["PTT", None, "SCB"])
    result = validate_and_clean(df)
    assert list(result.index) == [0, 1]
