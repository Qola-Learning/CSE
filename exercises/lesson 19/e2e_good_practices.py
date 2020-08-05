""" a simple end-to-end test automation framework using 
Object-Oriented principles (including demonstrating good coding practices) """

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#invoking webdriver
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# maximizes the current window
driver.maximize_window()

# enter url of the site
driver.get("https://demoblaze.com/")

#click on login button
driver.find_element_by_id("login2").click()

# wait for 3 seconds username to appear before clicking
usernameWait = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='loginusername']")))
usernameWait.send_keys("selorm");

# enter password
driver.find_element_by_id("loginpassword").send_keys("12345")

# click on login button 
driver.find_element_by_xpath("//button[contains(text(),'Log in')]").click()

# sleep for four seconds
time.sleep(4)

# click on Samsung galaxy s6
driver.find_element_by_link_text("Samsung galaxy s6").click()

# click on add to cart
addCart = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart")))
addCart.click();

# switch to handle javascript alert
alertOK = driver.switch_to.alert
# clicks 'OK' button
alertOK.accept()

