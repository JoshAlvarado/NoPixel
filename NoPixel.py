from re import T
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://store.nopixel.net/login')

time.sleep(5)
browser.find_element_by_link_text("LOGIN WITH FIVEM").click()
time.sleep(3)
browser.find_element_by_id("login-account-name").send_keys("USERNAME")
browser.find_element_by_id ("login-account-password").send_keys("PASSWORD")
browser.find_element_by_id("login-button").click()
time.sleep(5)
browser.find_element_by_xpath("/html/body/div/form/button").click()
time.sleep(1)

def check_package():
    browser.get('https://store.nopixel.net/package/4490800')
    time.sleep(3)
    browser.find_element_by_link_text("SUBSCRIBE").click()
    time.sleep(1)
    if "https://store.nopixel.net/checkout/basket" in browser.current_url:
        print("shit here")
        data = {'value1': "buy this shit"}
        requests.post("https://maker.ifttt.com/trigger/chores/with/key/INSERT IFTTT KEY FOR NOTIFACTION TO PHONE", json=data)
    elif "https://store.nopixel.net/" in browser.current_url:
        print("shit aint here")
        time.sleep(30)
        print("check again")
        check_package()
check_package()
time.sleep(4)
browser.close()
