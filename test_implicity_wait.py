from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    yield driver
    driver.quit()

def test_visible_after_with_implicit_wait(driver):
    driver.get('https://victoretc.github.io/selenium_waits/')
    tittle_h1 = driver.find_element(By.TAG_NAME, "h1")
    assert tittle_h1.text == 'Практика с ожиданиями в Selenium'
    start_testing_button = driver.find_element(By.CSS_SELECTOR, "button[id='startTest']")
    assert start_testing_button.text == 'Начать тестирование'
    # start_testing_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='startTest']")))
    # assert start_testing_button.text == 'Начать тестирование'
    # start_testing_button.click()
    # vissible_after_button = driver.find_element(By.XPATH, "//button[text()='Visible After 5 Seconds']")
    # assert vissible_after_button.is_displayed()