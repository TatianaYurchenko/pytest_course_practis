import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.freeconferencecall.com/global/pl/login")
login_field = driver.find_element("xpath", "//input[@id='login_email']")
login_field.send_keys("selenium@ya.ru")

password_field = driver.find_element("xpath", "//input[@type='password']")
password_field.send_keys("123")

agree_checkbox =  driver.find_element("xpath", "//input[@id='gdpr_checkbox']")
agree_checkbox.click()

submit_button = driver.find_element("xpath", "//button[@id='loginformsubmit']")
submit_button.click()

driver.get("https://www.freeconferencecall.com/profile/settings?tab=wall-editor")

# если загрузка файла реализована через button то где-то есть скрытый imput
#  и он находится по такой конструкции вот по такой конструкции ("xpath", "//input[@type='file']")
time.sleep(5)
upload_fild = driver.find_element("xpath", "//input[@type='file']")
time.sleep(5)
upload_fild.send_keys(f"{os.getcwd()}/downloads/2.PNG")
time.sleep(10)
