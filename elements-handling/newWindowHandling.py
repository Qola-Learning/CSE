''' This is a code which shows how to handle a new page when it is opened'''


from selenium import webdriver
import time


# invoking the webdriver
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# get the url
driver.get("http://the-internet.herokuapp.com/windows")

# click on click here
driver.find_element_by_link_text("Click Here").click()

# new window object
newWindow = driver.window_handles[1]
# switch to new window using 
driver.switch_to.window(newWindow)

# new window and print text using tag name
print(driver.find_element_by_xpath("//h3[contains(text(),'New Window')]").text)

# switch to parent window
parentWindow = driver.window_handles[0]

driver.switch_to.window(parentWindow)


# old window and print text using tag name
print(driver.find_element_by_tag_name("h3").text)

driver.quit()