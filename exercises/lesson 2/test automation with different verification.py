# test automation framework with different verifications
from selenium import webdriver
import time 

# invoking chromedriver to open chrome browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# get method to to open the url
driver.get("https://katalon-demo-cura.herokuapp.com/")

# maximize window
driver.maximize_window()

# make appointment
driver.find_element_by_id("btn-make-appointment").click()

# pause for 2 seconds
time.sleep(2)

# enter username
driver.find_element_by_id("txt-username").send_keys("John Doe")

# enter password
driver.find_element_by_name("password").send_keys("ThisIsNotAPassword")

# login
driver.find_element_by_id("btn-login").click()

# confirm appointment page after successful login
confirmation = driver.find_element_by_tag_name("h2")
assert confirmation.text == 'Make Appointment'


# click on bars
driver.find_element_by_xpath("//i[@class='fa fa-bars']").click()

# click on logout
driver.find_element_by_link_text("Logout").click()

# verify logout page
verify_logout = "CURA Healthcare Service"
assert success_text in self.driver.find_element_by_tag_name("h1").text


