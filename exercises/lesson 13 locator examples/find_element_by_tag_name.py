# find element by tag  name

from selenium import webdriver

# invoking chromedriver to open chrome browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# get method to to open the url
driver.get("http://the-internet.herokuapp.com/")

# find element by tag  name
driver.find_element_by_tag_name("h2").click()

# close driver
driver.quit()