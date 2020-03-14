from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://www.youtube.com/')


inputElement = browser.find_element_by_name("search_query").send_keys("Indian National Anthem")

browser.find_element_by_id("search-icon-legacy").click()
time.sleep(5)

browser.find_element_by_class_name("style-scope ytd-vertical-list-renderer").click()
time.sleep(10)

/*browser.find_element_by_class_name("ytp-ad-skip-button-container").click() 
time.sleep(2)


browser.find_element_by_class_name("ytp-mute-button ytp-button").click()
time.sleep(10)

browser.find_element_by_class_name("ytp-mute-button ytp-button").click()

browser.find_element_by_class_name("ytp-fullscreen-button ytp-button").click()
time.sleep(5)

browser.find_element_by_class_name("ytp-fullscreen-button ytp-button").click()

browser.find_element_by_class_name("ytp-size-button ytp-button").click()
time.sleep(2)
browser.find_element_by_class_name("ytp-size-button ytp-button").click()
time.sleep(1)

browser.find_element_by_class_name("ytp-miniplayer-button ytp-button").click()
time.sleep(5)
browser.send_keys("i")*/



