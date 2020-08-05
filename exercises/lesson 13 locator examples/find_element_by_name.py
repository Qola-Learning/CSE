# find element by id

from selenium import webdriver

# invoking chromedriver to open chrome browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# get method to to open the url
driver.get("https:google.com/")

# find element by name
driver.find_element_by_name("q").click()

# close driver
driver.quit()
