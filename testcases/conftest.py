import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def tc_setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    # wait = WebDriverWait(driver, 10)
    request.cls.driver = driver
    # request.cls.wait = wait
    yield
    driver.close()
