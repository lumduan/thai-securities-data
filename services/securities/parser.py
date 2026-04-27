import io

import pandas as pd
from pymonad.either import Either, Left, Right

_ROWS_TO_DROP = [0, 1]
_COLUMN_NAMES = ["symbol", "name", "market", "industry", "sector", "address", "zip", "tel", "fax", "web"]
_EXPECTED_COLUMNS = len(_COLUMN_NAMES)


def parse_html_to_df(
    html: str,
    rows_to_drop: list[int] = _ROWS_TO_DROP,
    column_names: list[str] = _COLUMN_NAMES,
) -> Either:
    """
    Parse raw SET HTML table into a cleaned DataFrame.
    Returns Right(pd.DataFrame) or Left(error_message).
    """
    try:
        tables = pd.read_html(io.StringIO(html))
    except ValueError as exc:
        return Left(f"No table found in HTML: {exc}")
    except Exception as exc:
        return Left(f"HTML parse error: {exc}")

    df = tables[0]

    if df.shape[1] != _EXPECTED_COLUMNS:
        return Left(
            f"Unexpected column count: expected {_EXPECTED_COLUMNS}, got {df.shape[1]}"
        )

    try:
        df = df.drop(index=rows_to_drop).reset_index(drop=True)
    except KeyError as exc:
        return Left(f"Cannot drop rows {rows_to_drop}: {exc}")

    df.columns = column_names

    try:
        df = validate_and_clean(df)
    except ValueError as exc:
        return Left(str(exc))

    return Right(df)


def validate_and_clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Strip whitespace, normalise dtypes, drop rows with null/empty symbols.
    Raises ValueError on fatal schema errors.
    """
    if "symbol" not in df.columns:
        raise ValueError("DataFrame is missing required 'symbol' column")

    for col in df.columns:
        if pd.api.types.is_string_dtype(df[col]) or df[col].dtype == object:
            df[col] = df[col].str.strip()

    df = df[df["symbol"].notna() & (df["symbol"] != "")].reset_index(drop=True)

    return df
