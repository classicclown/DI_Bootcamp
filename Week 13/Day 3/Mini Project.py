from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pprint  # To tidy up

options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
driver = webdriver.Chrome(options=options)

url = 'https://www.inmotionhosting.com/'
driver.get(url)


driver.implicitly_wait(10)


cards = driver.find_elements(By.CLASS_NAME, "imh-rostrum-card")
plan_list = []
is_first_row = True

for plan in cards:
    plan_name = plan.find_element(By.XPATH, './/h3').text
    plan_features = plan.find_element(By.XPATH,'.//div[1]').text

    try:
        # try the first price path for the first row only
        if is_first_row:
            plan_price = plan.find_element(By.XPATH, './/div[2]/div[2]/div').text
            is_first_row = False  # switch the flag for subsequent rows
        else:
            # use second price path for remaining rows
            plan_price = plan.find_element(By.XPATH, './/div[2]/div[1]/div').text
    except:
        # in case where neither path works like log error or assign placeholder
        plan_price = "Price Not Found"

    plan_item = {
        'Name': plan_name,
        'Feature': plan_features,
        'Price': plan_price
    }
    plan_list.append(plan_item)





