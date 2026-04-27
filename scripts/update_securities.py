"""
Entrypoint for the Thai Securities data update pipeline.
Run by GitHub Actions workflow; also runnable locally by setting env vars directly.

Exit codes:
  0 — success (both TH and EN processed)
  1 — partial or total failure (logged, GitHub Actions marks run as failed)
"""

import logging
import sys

from config import DATA_DIR, LOG_LEVEL, SET_URL_EN, SET_URL_TH
from services.securities.fetcher import fetch_securities_data
from services.securities.json_exporter import export_all
from services.securities.parser import parse_html_to_df

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)


def run_pipeline(url: str, encoding: str, lang_suffix: str) -> bool:
    """
    Run the full pipeline for one language.
    Returns True on success, False on failure.
    """
    logger.info("Fetching %s data from %s", lang_suffix.upper(), url)
    fetch_result = fetch_securities_data(url, encoding)
    if fetch_result.is_left():
        logger.error("Fetch failed [%s]: %s", lang_suffix, fetch_result.either(lambda e: e, None))
        return False

    html = fetch_result.either(None, lambda v: v)
    logger.info("Fetch succeeded [%s], parsing HTML", lang_suffix.upper())

    parse_result = parse_html_to_df(html)
    if parse_result.is_left():
        logger.error("Parse failed [%s]: %s", lang_suffix, parse_result.either(lambda e: e, None))
        return False

    df = parse_result.either(None, lambda v: v)
    logger.info("Parsed %d rows [%s], exporting JSON", len(df), lang_suffix.upper())

    try:
        written = export_all(df, DATA_DIR, lang_suffix)
    except (IOError, OSError) as exc:
        logger.error("Export failed [%s]: %s", lang_suffix, exc)
        return False

    for name, path in written.items():
        logger.info("Wrote [%s] %s → %s", lang_suffix, name, path)

    return True


def main() -> None:
    results = {
        "th": run_pipeline(SET_URL_TH, "tis-620", "th"),
        "en": run_pipeline(SET_URL_EN, "tis-620", "en"),
    }

    failed = [lang for lang, ok in results.items() if not ok]
    if failed:
        logger.error("Pipeline failed for: %s", ", ".join(failed))
        sys.exit(1)

    logger.info("Pipeline complete — all languages exported to %s", DATA_DIR)


if __name__ == "__main__":
    main()
