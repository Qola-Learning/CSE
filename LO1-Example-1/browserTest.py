from selenium import webdriver

# invoking chrome's executable file to trigger browser
driver = webdriver.Chrome(executable_path="C:\\Users\onray\OneDrive\Documents\webdrivers\chromedriver.exe")

# opening this url in the browser
driver.get("https://www.google.com/")

driver.quit()