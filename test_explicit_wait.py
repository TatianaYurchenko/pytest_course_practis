import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    return driver

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait
def test_visible_after_with_explicit_waits(driver, wait):
    driver.get('https://victoretc.github.io/selenium_waits/')
    tittle_h1 = driver.find_element(By.TAG_NAME, "h1")
    assert tittle_h1.text == 'Практика с ожиданиями в Selenium'
    start_testing_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='startTest']")))
    assert start_testing_button.text == 'Начать тестирование'
    start_testing_button.click()
    # time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "input[id='login']").send_keys("login")
    driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("password")
    driver.find_element(By.CSS_SELECTOR, "input[id='agree']").click()
    driver.find_element(By.CSS_SELECTOR, "button[id='register']").click()
    spinner = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='loader']")))
    assert spinner.is_displayed()
    success_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p[id='successMessage']")))
    # success_message = driver.find_element(By.CSS_SELECTOR, "p[id='successMessage']")
    # assert success_message_text.is_enabled()
    assert success_message.text == 'Вы успешно зарегистрированы!'