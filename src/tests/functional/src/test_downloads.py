from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from adapters.watchdog.handlers import PartialDownloadHandler
from core import settings
from utils.decorators import telegram_notify_if_test_failed
from utils.utils import is_file_downloaded


@telegram_notify_if_test_failed
def test_download_python(driver, test_logger):
    test_logger.info("running test_download_python")
    driver.get(settings.SITE_URL)
    web_driver_waiter = WebDriverWait(
        driver=driver, timeout=settings.WEB_WAITER_DEFAULT_TIMEOUT
    )
    actions = ActionChains(driver)
    download_element = web_driver_waiter.until(
        EC.presence_of_element_located((By.ID, "downloads"))
    )
    actions.move_to_element(download_element).perform()
    download_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".download-os-source .button"))
    )
    download_button.click()
    is_download = is_file_downloaded(directory_path=settings.DOWNLOADS_DIR, handler=PartialDownloadHandler("Python-"))
    assert is_download
    test_logger.info("test_download_python passed successfully!")
