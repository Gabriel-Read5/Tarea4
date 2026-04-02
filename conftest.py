import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        driver = item.funcargs.get("driver", None)
        if driver is not None:
            os.makedirs("screenshots", exist_ok=True)
            test_name = item.name

            if rep.failed:
                driver.save_screenshot(f"screenshots/{test_name}_FAIL.png")
            else:
                driver.save_screenshot(f"screenshots/{test_name}_PASS.png")