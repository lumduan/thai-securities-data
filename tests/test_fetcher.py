import pytest
import requests
import responses as responses_lib

from services.securities.fetcher import fetch_securities_data

_URL = "https://www.set.or.th/dat/eod/listedcompany/static/listedCompanies_en_US.xls"


@responses_lib.activate
def test_fetch_returns_right_on_200():
    body = "<table><tr><td>Symbol</td></tr></table>"
    responses_lib.add(responses_lib.GET, _URL, body=body.encode("tis-620"), status=200)

    result = fetch_securities_data(_URL, encoding="tis-620")

    assert result.is_right()
    assert "Symbol" in result.value


@responses_lib.activate
def test_fetch_decodes_tis620():
    thai = "หลักทรัพย์"
    responses_lib.add(responses_lib.GET, _URL, body=thai.encode("tis-620"), status=200)

    result = fetch_securities_data(_URL, encoding="tis-620")

    assert result.is_right()
    assert thai in result.value


@responses_lib.activate
def test_fetch_returns_left_on_404():
    responses_lib.add(responses_lib.GET, _URL, status=404)

    result = fetch_securities_data(_URL)

    assert result.is_left()
    assert "404" in result.monoid[0]


@responses_lib.activate
def test_fetch_returns_left_on_500():
    responses_lib.add(responses_lib.GET, _URL, status=500)

    result = fetch_securities_data(_URL)

    assert result.is_left()
    assert "500" in result.monoid[0]


@responses_lib.activate
def test_fetch_returns_left_on_connection_error():
    responses_lib.add(responses_lib.GET, _URL, body=requests.exceptions.ConnectionError("refused"))

    result = fetch_securities_data(_URL)

    assert result.is_left()
    assert "Network error" in result.monoid[0]


@responses_lib.activate
def test_fetch_returns_left_on_timeout():
    responses_lib.add(responses_lib.GET, _URL, body=requests.exceptions.Timeout())

    result = fetch_securities_data(_URL)

    assert result.is_left()
    assert "Network error" in result.monoid[0]


def test_fetch_returns_left_on_unknown_encoding():
    with responses_lib.RequestsMock() as rsps:
        rsps.add(responses_lib.GET, _URL, body=b"data", status=200)
        result = fetch_securities_data(_URL, encoding="not-a-real-encoding")

    assert result.is_left()
    assert "encoding" in result.monoid[0].lower()
