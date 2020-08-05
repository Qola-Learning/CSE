# find element by id

from selenium import webdriver

# invoking chromedriver to open chrome browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# get method to to open the url
driver.get("https://katalon-demo-cura.herokuapp.com/")

# find element by id
driver.find_element_by_id("btn-make-appointment").click()

# close driver
driver.quit()
