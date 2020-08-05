# find element by partial link

from selenium import webdriver

# invoking chromedriver to open chrome browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# get method to to open the url
driver.get("http://the-internet.herokuapp.com/")

# find element by partial linktext
driver.find_element_by_partial_link_text("Hove").click()

# close driver
driver.quit()
