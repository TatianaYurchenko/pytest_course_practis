
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time


def test_add_item_to_cart(driver, wait):
    # driver.get("https://www.saucedemo.com/")
    # username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    # username_field.send_keys("standard_user")
    #
    # password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    # password_field.send_keys("secret_sauce")
    #
    # login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    # login_button.click()
    a = login()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    driver.find_element(By.CSS_SELECTOR, 'button[id="add-to-cart-sauce-labs-backpack"]').click()
    # посмотреть что товар добавился в корзину
    driver.find_element(By.CSS_SELECTOR, 'a[class ="shopping_cart_link"]').click()
    item = driver.find_element(By.CSS_SELECTOR, 'div[class="cart_quantity"]')
    assert item.text == '1'

    driver.quit()

def test_loguot(driver, wait):
    driver.get("https://www.saucedemo.com/")
    url_before = driver.current_url
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    wait.until(EC.element_to_be_clickable((By.ID, 'react-burger-menu-btn'))).click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#logout_sidebar_link'))).click()

    url_after = driver.current_url
    assert url_before == url_after
