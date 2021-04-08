

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

default_url = "https://tas.nutrislice.com/menu/tas/serving-line"
driver.get(default_url)

html = driver.find_element_by_xpath("/html")
print(html)

# timeout = 5

# try:
#     button = EC.presence_of_element_located((By.CLASS_NAME, 'primary'))
#     WebDriverWait(driver, timeout).until(button)
# except TimeoutException:
#     print("Timed out waiting for page to load")
# finally:
#     driver.find_element(By.XPATH, "/html/body/main/div/div[4]/button").click();
#     print("Page loaded")

# body = driver.find_element(By.XPATH, "/html/body") 
# main = body.find_element(By.TAG_NAME, "main")
# main.find_element(By.PARTIAL_LINK_TEXT, "Menus").click()

# print("go to next page")

# def get_context():


# body = driver.find_element(By.XPATH, "/html/body") 
# main = body.find_element(By.TAG_NAME, "main")
# main.find_element(By.TAG_NAME, "button").click()
# time.sleep(0.5)

# body = driver.find_element(By.XPATH, "/html/body") 
# main = body.find_element(By.TAG_NAME, "main")
# list_container = main.find_element(By.CLASS_NAME, "list-container")
# a = list_container.find_element(By.TAG_NAME, "a")

# print(a)





# import requests

# url ='https://tas.nutrislice.com/menu/menus-eula'
# html = requests.get(url)
# print(html.text)