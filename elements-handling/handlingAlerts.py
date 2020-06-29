'''this code demonstares how to handle javascript alerts'''


from selenium import webdriver


# invoking the webdriver
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# get the url
driver.get("http://the-internet.herokuapp.com/javascript_alerts")

# click on javascript alerts
driver.find_element_by_xpath("//button[contains(text(),'Click for JS Alert')]").click()

# switch to alert
jsAlert = driver.switch_to.alert
# accept the alert
jsAlert.accept()

driver.close()
