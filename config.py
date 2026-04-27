import os

SET_URL_TH: str = os.getenv(
    "SET_URL_TH",
    "https://www.set.or.th/dat/eod/listedcompany/static/listedCompanies_th_TH.xls",
)

SET_URL_EN: str = os.getenv(
    "SET_URL_EN",
    "https://www.set.or.th/dat/eod/listedcompany/static/listedCompanies_en_US.xls",
)

DATA_DIR: str = os.getenv("DATA_DIR", ".")

LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
