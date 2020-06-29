'''  this line of of code demonstrates how to locate 
      an element using using different locators
 '''
from selenium import webdriver

# invoking the chromedriver
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# maximizes the current window
driver.maximize_window()

# get method to enter our url
driver.get("https://qola.io/community/")

# entering our first name
driver.find_element_by_name("firstname").send_keys("Kofi")

# entering our second name
driver.find_element_by_name("lastname").send_keys("Kwame")

# entering our email address
driver.find_element_by_xpath("//input[@name='email']").send_keys("seah@qola.io")

# entering our city
driver.find_element_by_name("field[1]").send_keys("Accra")

# entering our country
driver.find_element_by_name("field[2]").send_keys("Ghana")

# entering phone number
driver.find_element_by_name("phone").send_keys("+233 24 444 4444")

# hit on 'JOIN THE COMMUNITY ' button
driver.find_element_by_class_name("_submit").click()