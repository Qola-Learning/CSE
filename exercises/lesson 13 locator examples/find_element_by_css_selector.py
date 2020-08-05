# find element by css selector
from selenium import webdriver

# invoking chromedriver to open chrome browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# get method to to open the url
driver.get("http://the-internet.herokuapp.com/")

# find element by css selector 
driver.find_element_by_css_selector("div.row:nth-child(2) div.large-12.columns:nth-child(2) ul:nth-child(4) li:nth-child(1) > a:nth-child(1)").click()

# close driver
driver.quit()