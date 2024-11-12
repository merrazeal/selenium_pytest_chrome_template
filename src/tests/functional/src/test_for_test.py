from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core import settings
from utils.decorators import telegram_notify_if_test_failed


@telegram_notify_if_test_failed
def test_for_test(driver, test_logger):
    test_logger.info("running test for test =)")
    driver.get(settings.SITE_URL)
    web_driver_waiter = WebDriverWait(
        driver=driver, timeout=settings.WEB_WAITER_DEFAULT_TIMEOUT
    )
    intro = web_driver_waiter.until(
        EC.presence_of_element_located((By.CLASS_NAME, "introduction"))
    )
    assert intro.text.startswith(
        "Python is a programming language that lets you work quickly"
    )
    test_logger.info("test_for_test passed successfully!")
