# find element by id

from selenium import webdriver

# invoking chromedriver to open chrome browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# get method to to open the url
driver.get("http://the-internet.herokuapp.com/")

# find element by linktext
driver.find_element_by_link_text("Frames").click()

# close driver
driver.quit()
