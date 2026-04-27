import requests
from pymonad.either import Either, Left, Right

_HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; thai-securities-data/1.0)"}
_TIMEOUT = 30


def fetch_securities_data(url: str, encoding: str = "tis-620") -> Either:
    """
    Fetch raw HTML from the SET website.
    Returns Right(html_str) or Left(error_message).
    """
    try:
        response = requests.get(url, headers=_HEADERS, timeout=_TIMEOUT)
    except requests.exceptions.RequestException as exc:
        return Left(f"Network error fetching {url}: {exc}")

    if response.status_code != 200:
        return Left(
            f"Unexpected status {response.status_code} fetching {url}"
        )

    try:
        html = response.content.decode(encoding, errors="replace")
    except LookupError as exc:
        return Left(f"Unknown encoding '{encoding}': {exc}")

    return Right(html)
