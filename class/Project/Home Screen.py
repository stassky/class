from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("c:\\users\stas\chromedriver.exe")
driver.implicitly_wait(15)
################## Choose a Businesss Screen ##################################

driver.get("https:\\buyme.co.il/search?budget=3&category=16&region=9")                              # Enter businesses screen
elements = driver.find_elements_by_xpath("//a[@class='poster ']")                                   # click on the business
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/a[6]/div/div[2]").click()  # Name the price
driver.find_element_by_id("ember937").send_keys("200")                                              # sending price
driver.find_element_by_class_name("btn-wrapper").click()                                            # Submit (submit function is no go for me)

######################### Sender & Receiver information screen #################

