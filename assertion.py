# this test scrip demonstrates how to use assertions in testing a web page.

from selenium import webdriver


driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
# maximize browser
driver.maximize_window()

# get url
driver.get("http://automationpractice.com/index.php")

# sign in
driver.find_element_by_xpath("//a[@class='login']").click()

# enter email address
driver.find_element_by_css_selector("#email").send_keys("selormonray14@gmail.com")

# enter your password
driver.find_element_by_css_selector("#passwd").send_keys("abcd1234")

# click on signin button 
driver.find_element_by_name("SubmitLogin").click()

# verify account page
verify_login_text = driver.find_element_by_class_name("info-account")
assert verify_login_text.text == "Welcome to your account. Here you can manage all of your personal information and orders."

driver.quit()