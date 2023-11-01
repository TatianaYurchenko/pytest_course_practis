import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# У вас виндовс видимо, добавьте
#
# preferences = {
#     "download.default_directory": download_folder,
#     "download.prompt_for_download": False,
#     "download.directory_upgrade": True,
#     "safebrowsing.enabled": True
# }

from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
# строка для скачивания файлов
# для скачивания файлов в необходимую нам директорию используется словарь prefs
prefs = {
    "download.default_directory": f"{os.getcwd()}\downloads",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
# строка для скачивания файлов/ prefs зарезервированное имя которое говорит о том что experimental_option
# будет подтягивать preferenses/ второй аргумент это наш словарь

chrome_options.add_experimental_option("prefs", prefs)
# chrome_options.add_argument('--window-size=2880,1800')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
time.sleep(3)
driver.get("https://the-internet.herokuapp.com/download")
driver.find_elements("xpath", "//a")[3].click()
time.sleep(3)
