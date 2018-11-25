from selenium import webdriver
driver = webdriver.Firefox(executable_path="D:\Selenium\geckodriver.exe")
driver.get("https://translate.google.com/")

print(driver.current_url)

print(driver.title)

print(driver.page_source)                   # מדפיס Source של העמוד
driver.refresh()                            # ריענון עמוד
driver.find_element_by_id("gt-submit")      # למצוא את הכפתור של התרגום

#my_list = driver.find_element_by_id("gt-submit")      # נותנים לכל המשתנים שם של רשימה

driver.find_element_by_id("source").send_keys("Whatsupp")
#   driver.find_element_by_xpath("//input[@tabindex='0']")

x = driver.find_elements_by_id("123")                          # תמצא את כל האלמנטים שה ID שלהם הוא 123
x[0].click()                                                   #  תלחץ על התוצאה באינדקס במקום 0

driver.find_element_by_id("gt-submit").click()

button_element = driver.find_element_by_id("gt-submit")
button_element.click()
driver.quit()
#kugmh