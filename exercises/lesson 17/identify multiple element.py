# Use Selenium with Python to identify multiple elements on a webpage

from selenium import webdriver
# from selenium.webdriver.common.by import By

# invoking chromedriver to open chrome browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# maximize page
driver.maximize_window()

# get method to to open the url
driver.get("https://demoblaze.com/")

# find element by class  name
categories = driver.find_elements_by_css_selector("#itemc")

# print list of categories
for category in categories:
    print(category.text)

# close driver
driver.quit()



