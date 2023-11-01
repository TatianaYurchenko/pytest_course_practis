import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/upload")

# обычно файлы для загрузки через кнопку реализоны по типу , обязательно с  тегом input и атрибутом type='file'

upload_fild = driver.find_element("xpath", "//input[@type='file']")
upload_fild.send_keys(f"{os.getcwd()}/downloads/2.PNG")

