# this is a simple test automation verifying the presence of the text 'images' 


from selenium import webdriver

# invoking the chrome driver
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# entering url of the site to be tested
driver.get("https://google.com")

# clicking on the Images link text
driver.find_element_by_link_text("Images").click()

# verifying the the page contains images
if driver.page_source.__contains__("images"):
    print("Text is present")
else:
    print("text is absent")


driver.find_element_by_name()

# close the driver
driver.quit()
