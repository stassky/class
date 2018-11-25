from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome("c:\\users\stas\chromedriver.exe")                # Define working with Chrome
driver.implicitly_wait(15)                                                  # 15 secs of grace :)

driver.get("https:\\buyme.co.il")
print("Current site is: ",driver.current_url)                               # printing Site`s address
Text_Url = (driver.current_url)

My_File = open("D:\\פרוייקט סלניום.txt",'w')                                # Creating(!) a new txt file
My_File.write(Text_Url)                                                     # writing address to file

################################ Here we go #########################################################
driver.find_element_by_class_name("seperator-link").click()
driver.find_element_by_class_name("header-link").click()
