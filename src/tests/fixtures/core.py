import logging
from logging.config import dictConfig

import pytest
from selenium import webdriver

from core import logger, settings


@pytest.fixture
def service():
    service = webdriver.ChromeService(executable_path=settings.CHROMEDRIVER_PATH)
    yield service
    service.stop()


@pytest.fixture
def options():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920, 1080")
    options.add_argument("--headless=new")
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")
    return options


@pytest.fixture
def driver(options, service):
    driver = webdriver.Chrome(options=options, service=service)
    driver.execute_cdp_cmd(
        "Page.setDownloadBehavior",
        {"behavior": "allow", "downloadPath": settings.DOWNLOADS_DIR},
    )
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def test_logger():
    dictConfig(logger.LOGGING)
    return logging.getLogger("test")
