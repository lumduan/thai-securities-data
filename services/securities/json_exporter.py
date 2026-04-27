import json
import os
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from config import SET_URL_EN, SET_URL_TH

_REPO_RAW_BASE = "https://raw.githubusercontent.com/lumduan/thai-securities-data/main"
_COMPACT_COLS = ["symbol", "name", "market", "sector"]
_SCHEMA = {
    "symbol": "Stock symbol (primary key)",
    "name": "Company name",
    "market": "Market (SET, mai, etc.)",
    "industry": "Industry classification",
    "sector": "Sector classification",
    "address": "Company address",
    "zip": "Postal code",
    "tel": "Telephone number",
    "fax": "Fax number",
    "web": "Website URL",
}


def export_all(df: pd.DataFrame, output_dir: str, lang_suffix: str) -> dict[str, str]:
    """
    Export all 6 JSON formats for one language to output_dir.
    Returns dict mapping format name → file path.
    Raises IOError if any file cannot be written.
    """
    base = Path(output_dir)
    paths = {
        "all": base / f"thai_securities_all_{lang_suffix}.json",
        "compact": base / f"thai_securities_compact_{lang_suffix}.json",
        "by_sector": base / f"thai_securities_by_sector_{lang_suffix}.json",
        "market_set": base / f"thai_securities_market_set_{lang_suffix}.json",
        "market_mai": base / f"thai_securities_market_mai_{lang_suffix}.json",
        "metadata": base / f"metadata_{lang_suffix}.json",
    }

    _export_all_records(df, paths["all"])
    _export_compact(df, paths["compact"])
    _export_by_sector(df, paths["by_sector"])
    _export_by_market(df, "SET", paths["market_set"])
    _export_by_market(df, "mai", paths["market_mai"])
    _export_metadata(df, lang_suffix, paths["metadata"])

    return {name: str(path) for name, path in paths.items()}


def _write_json(data: object, path: Path) -> None:
    try:
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except OSError as exc:
        raise IOError(f"Failed to write {path}: {exc}") from exc


def _export_all_records(df: pd.DataFrame, path: Path) -> None:
    _write_json(df.to_dict(orient="records"), path)


def _export_compact(df: pd.DataFrame, path: Path) -> None:
    cols = [c for c in _COMPACT_COLS if c in df.columns]
    _write_json(df[cols].to_dict(orient="records"), path)


def _export_by_sector(df: pd.DataFrame, path: Path) -> None:
    grouped: dict[str, list] = {}
    for sector, group in df.groupby("sector", sort=True):
        grouped[sector] = group.to_dict(orient="records")
    _write_json(grouped, path)


def _export_by_market(df: pd.DataFrame, market_name: str, path: Path) -> None:
    filtered = df[df["market"] == market_name]
    _write_json(filtered.to_dict(orient="records"), path)


def _export_metadata(df: pd.DataFrame, lang_suffix: str, path: Path) -> None:
    market_counts = df["market"].value_counts().to_dict()
    sector_counts = df["sector"].value_counts().sort_index().to_dict()
    data_source = SET_URL_TH if lang_suffix == "th" else SET_URL_EN
    last_updated = datetime.now(timezone.utc).replace(tzinfo=None).isoformat()

    metadata = {
        "last_updated": last_updated,
        "total_securities": len(df),
        "markets": {k: int(v) for k, v in market_counts.items()},
        "sectors": {k: int(v) for k, v in sector_counts.items()},
        "data_source": data_source,
        "api_endpoints": {
            "all_securities": f"{_REPO_RAW_BASE}/thai_securities_all_{lang_suffix}.json",
            "compact": f"{_REPO_RAW_BASE}/thai_securities_compact_{lang_suffix}.json",
            "metadata": f"{_REPO_RAW_BASE}/metadata_{lang_suffix}.json",
            "by_sector": f"{_REPO_RAW_BASE}/thai_securities_by_sector_{lang_suffix}.json",
            "market_set": f"{_REPO_RAW_BASE}/thai_securities_market_set_{lang_suffix}.json",
            "market_mai": f"{_REPO_RAW_BASE}/thai_securities_market_mai_{lang_suffix}.json",
        },
        "export_info": {
            "generated_by": "thai-securities-data JSON Exporter",
            "files_exported": ["all", "market_set", "market_mai", "by_sector"],
            "schema": _SCHEMA,
        },
    }
    _write_json(metadata, path)
