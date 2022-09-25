from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
Path = "/home/ammar/Downloads/chromedriver"
driver = webdriver.Chrome(Path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(2)


action = ActionChains(driver)


language = driver.find_element_by_id("langSelect-EN")

items = [driver.find_element_by_id("productPrice" + str(i))
         for i in range(1, -1, -1)]

cookie_count = driver.find_element_by_id("cookies")

action.click(language)
action.perform()


for i in range(5000):
    cookie = driver.find_element_by_id('bigCookie')
    cookie.click()
    cookieCount = int(driver.find_element_by_id(
        'cookies').text.split(' ')[0].replace(',', ''))
    print(cookieCount)
