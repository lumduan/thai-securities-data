import json
from pathlib import Path

import pandas as pd
import pytest

from services.securities.json_exporter import export_all

_COLUMNS = ["symbol", "name", "market", "industry", "sector", "address", "zip", "tel", "fax", "web"]

_ROWS = [
    ["PTT",  "PTT PUBLIC COMPANY LIMITED",      "SET", "Resources",         "Energy & Utilities",   "555 Vibhavadi", "10900", "0-2537-2000", "0-2537-3498", "www.ptt.or.th"],
    ["SCB",  "SIAM COMMERCIAL BANK PCL",        "SET", "Financials",        "Banking",              "9 Ratchadapisek", "10400", "0-2777-7777", "0-2777-7477", "www.scb.co.th"],
    ["KBANK","KASIKORNBANK PCL",                "SET", "Financials",        "Banking",              "1 Rat Burana", "10140", "0-2888-8888", "0-2888-8882", "www.kasikornbank.com"],
    ["AOT",  "AIRPORTS OF THAILAND PCL",        "SET", "Services",          "Transportation & Logistics", "333 Chert Wudthakas", "10210", "0-2535-1111", "0-2535-4060", "www.airportthai.co.th"],
    ["THB1", "THAI BAHT FUND",                  "mai", "Financial Products", "-",                   "100 Sukhumvit", "10110", "0-2123-4567", "0-2123-4568", "www.thaifund.co.th"],
]


def _make_df() -> pd.DataFrame:
    return pd.DataFrame(_ROWS, columns=_COLUMNS)


_EXPECTED_FILES = {
    "en": [
        "thai_securities_all_en.json",
        "thai_securities_compact_en.json",
        "thai_securities_by_sector_en.json",
        "thai_securities_market_set_en.json",
        "thai_securities_market_mai_en.json",
        "metadata_en.json",
    ],
    "th": [
        "thai_securities_all_th.json",
        "thai_securities_compact_th.json",
        "thai_securities_by_sector_th.json",
        "thai_securities_market_set_th.json",
        "thai_securities_market_mai_th.json",
        "metadata_th.json",
    ],
}


# ── export_all: file existence ────────────────────────────────────────────────

@pytest.mark.parametrize("lang", ["en", "th"])
def test_export_all_creates_six_files(tmp_path, lang):
    export_all(_make_df(), str(tmp_path), lang)
    for fname in _EXPECTED_FILES[lang]:
        assert (tmp_path / fname).exists(), f"Missing: {fname}"


def test_export_all_returns_six_paths(tmp_path):
    result = export_all(_make_df(), str(tmp_path), "en")
    assert set(result.keys()) == {"all", "compact", "by_sector", "market_set", "market_mai", "metadata"}
    for path in result.values():
        assert Path(path).exists()


# ── all_records ───────────────────────────────────────────────────────────────

def test_all_records_is_list_of_dicts(tmp_path):
    export_all(_make_df(), str(tmp_path), "en")
    data = json.loads((tmp_path / "thai_securities_all_en.json").read_text())
    assert isinstance(data, list)
    assert len(data) == 5
    assert set(data[0].keys()) == set(_COLUMNS)


def test_all_records_thai_chars_readable(tmp_path):
    df = _make_df()
    df.loc[0, "name"] = "บริษัท ปตท. จำกัด (มหาชน)"
    export_all(df, str(tmp_path), "th")
    raw = (tmp_path / "thai_securities_all_th.json").read_text(encoding="utf-8")
    assert "บริษัท" in raw  # not \\uXXXX escaped


# ── compact ───────────────────────────────────────────────────────────────────

def test_compact_has_only_four_cols(tmp_path):
    export_all(_make_df(), str(tmp_path), "en")
    data = json.loads((tmp_path / "thai_securities_compact_en.json").read_text())
    assert isinstance(data, list)
    assert len(data) == 5
    assert set(data[0].keys()) == {"symbol", "name", "market", "sector"}


# ── by_sector ─────────────────────────────────────────────────────────────────

def test_by_sector_is_dict_keyed_by_sector(tmp_path):
    export_all(_make_df(), str(tmp_path), "en")
    data = json.loads((tmp_path / "thai_securities_by_sector_en.json").read_text())
    assert isinstance(data, dict)
    assert "Banking" in data
    assert "Energy & Utilities" in data


def test_by_sector_records_are_full_rows(tmp_path):
    export_all(_make_df(), str(tmp_path), "en")
    data = json.loads((tmp_path / "thai_securities_by_sector_en.json").read_text())
    banking = data["Banking"]
    assert len(banking) == 2  # SCB + KBANK
    assert set(banking[0].keys()) == set(_COLUMNS)


# ── market files ──────────────────────────────────────────────────────────────

def test_market_set_contains_only_set(tmp_path):
    export_all(_make_df(), str(tmp_path), "en")
    data = json.loads((tmp_path / "thai_securities_market_set_en.json").read_text())
    assert all(r["market"] == "SET" for r in data)
    assert len(data) == 4


def test_market_mai_contains_only_mai(tmp_path):
    export_all(_make_df(), str(tmp_path), "en")
    data = json.loads((tmp_path / "thai_securities_market_mai_en.json").read_text())
    assert all(r["market"] == "mai" for r in data)
    assert len(data) == 1


# ── metadata ──────────────────────────────────────────────────────────────────

def test_metadata_top_level_keys(tmp_path):
    export_all(_make_df(), str(tmp_path), "en")
    meta = json.loads((tmp_path / "metadata_en.json").read_text())
    for key in ("last_updated", "total_securities", "markets", "sectors", "data_source", "api_endpoints", "export_info"):
        assert key in meta, f"Missing key: {key}"


def test_metadata_total_securities(tmp_path):
    export_all(_make_df(), str(tmp_path), "en")
    meta = json.loads((tmp_path / "metadata_en.json").read_text())
    assert meta["total_securities"] == 5


def test_metadata_market_counts(tmp_path):
    export_all(_make_df(), str(tmp_path), "en")
    meta = json.loads((tmp_path / "metadata_en.json").read_text())
    assert meta["markets"]["SET"] == 4
    assert meta["markets"]["mai"] == 1


def test_metadata_api_endpoints_keys(tmp_path):
    export_all(_make_df(), str(tmp_path), "en")
    meta = json.loads((tmp_path / "metadata_en.json").read_text())
    assert set(meta["api_endpoints"].keys()) == {
        "all_securities", "compact", "metadata", "by_sector", "market_set", "market_mai"
    }


def test_metadata_api_endpoints_use_lang_suffix(tmp_path):
    export_all(_make_df(), str(tmp_path), "th")
    meta = json.loads((tmp_path / "metadata_th.json").read_text())
    for url in meta["api_endpoints"].values():
        assert "_th.json" in url or url.endswith("metadata_th.json")


def test_metadata_data_source_en(tmp_path):
    export_all(_make_df(), str(tmp_path), "en")
    meta = json.loads((tmp_path / "metadata_en.json").read_text())
    assert "en_US" in meta["data_source"]


def test_metadata_data_source_th(tmp_path):
    export_all(_make_df(), str(tmp_path), "th")
    meta = json.loads((tmp_path / "metadata_th.json").read_text())
    assert "th_TH" in meta["data_source"]


def test_metadata_last_updated_is_iso_string(tmp_path):
    export_all(_make_df(), str(tmp_path), "en")
    meta = json.loads((tmp_path / "metadata_en.json").read_text())
    assert isinstance(meta["last_updated"], str)
    assert "T" in meta["last_updated"]  # ISO 8601 datetime separator


# ── output_dir defaults ───────────────────────────────────────────────────────

def test_export_all_accepts_dot_as_output_dir(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    export_all(_make_df(), ".", "en")
    assert (tmp_path / "thai_securities_all_en.json").exists()
