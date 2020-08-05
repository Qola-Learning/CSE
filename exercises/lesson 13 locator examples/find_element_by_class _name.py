# find element by class  name

from selenium import webdriver

# invoking chromedriver to open chrome browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# get method to to open the url
driver.get("http://the-internet.herokuapp.com/")

# find element by class  name
driver.find_element_by_class_name("heading").click()

# close driver
driver.quit()