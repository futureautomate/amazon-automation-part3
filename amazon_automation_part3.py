# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 23:51:04 2020

@author: Tejas
"""

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import logindata
from mailpy import send_email

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('F:\Channel\webdriver\chromedriver.exe', chrome_options=options)
action = ActionChains(driver)
time.sleep(1)


driver.get('http://www.amazon.in')
time.sleep(3)
 
firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span/span')
action.move_to_element(firstLevelMenu).perform()
time.sleep(3)
 
secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
secondLevelMenu.click()
time.sleep(3)

signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')
signinelement.send_keys(logindata.USERNAME)
time.sleep(3)

cont = driver.find_element_by_xpath('//*[@id="continue"]')
cont.click()
time.sleep(3)

passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')
passwordelement.send_keys(logindata.PASSWORD)
time.sleep(3)

login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
login.click()
time.sleep(3)

'----------------------------X-------------------------X------------------------------------------------'

reutrnorder = driver.find_element_by_xpath('//*[@id="nav-orders"]')
reutrnorder.click()
time.sleep(3)

trackpackage = driver.find_element_by_xpath('//*[@id="a-autoid-3-announce"]')
trackpackage.click()
time.sleep(3)

shippingdetails = driver.find_element_by_link_text('See all updates')
shippingdetails.click()  
time.sleep(3)

container = driver.find_element_by_id('tracking-events-container')
time.sleep(3)

trackingData = container.find_elements_by_css_selector('div.a-spacing-top-medium')
time.sleep(3)

trackingList = []

for item in trackingData:
    trackingList.append((item.text).split('\n'))

time.sleep(3)

subject = "Tracking Detials"
send_email(subject, trackingList)