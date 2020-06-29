# this code shows how the various each of the various webdrivers interact and invoke their resective browsers



from selenium import webdriver

# invoking chromedriver to open chrome browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# get method to to open the url
driver.get("https://google.com")

# close browser
driver.quit()




# invoking geckodriver to open firefox browser
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

# get method to to open the url
driver.get("https://google.com")

# close browser
driver.quit()



# invoking msedgedriver to open microsoft edge browser
driver = webdriver.Edge(executable_path="C:\\msedgedriver.exe")

# get method to to open the url
driver.get("https://google.com")

# close browser
driver.quit()



