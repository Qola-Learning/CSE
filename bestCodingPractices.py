''' in this piece of code, there are various techniques used that ensures good coding practices'''


from selenium import webdriver
import time


# invoking the webdriver
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

# maxiximize the window
driver.maximize_window()

# get the url
driver.get("http://automationpractice.com/index.php")

# sign in
driver.find_element_by_xpath("//a[@class='login']").click()

# enter email address
driver.find_element_by_css_selector("#email").send_keys("selormonray14@gmail.com")

# enter your password
driver.find_element_by_css_selector("#passwd").send_keys("abcd1234")

# click on signin button 
driver.find_element_by_name("SubmitLogin").click()



# click to to to the homepage
driver.find_element_by_id("header_logo").click()


# wait for two seconds
time.sleep(2)



# buying faded short sleeves
# click on item
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/a[1]/img[1]").click()

# add to cart
driver.find_element_by_xpath("//span[contains(text(),'Add to cart')]").click()

# sleep for four seconds
time.sleep(4)

# continue shopping
driver.find_element_by_xpath("//span[@class='continue btn btn-default button exclusive-medium']//span[1]").click()

# go back to the homepage
driver.find_element_by_id("//div[@id='header_logo']").click()

# wait for two seconds
time.sleep(2)



# buying blouse
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[2]/div[1]/div[1]/div[1]/a[1]/img[1]").click()

# add item to cart
driver.find_element_by_xpath("//span[contains(text(),'Add to cart')]").click()

# wait for four seconds
time.sleep(4)

# continue shopping
driver.find_elements_by_xpath("//span[@class='continue btn btn-default button exclusive-medium']//span[1]").click()

# go back to homepage
driver.find_element_by_id("//div[@id='header_logo']").click()





# buying printed summer dress
# printed summer dress
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[5]/div[1]/div[1]/div[1]/a[1]/img[1]").click()

# add item to cart
driver.find_element_by_xpath("//span[contains(text(),'Add to cart')]").click()

# wait for four seconds
time.sleep(4)

# proceed to checkout
driver.find_element_by_xpath("//span[contains(text(),'Proceed to checkout')]").click()



# second checkout
driver.find_element_by_xpath("//a[@class='button btn btn-default standard-checkout button-medium']//span[contains(text(),'Proceed to checkout')]").click()

# third checkout
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/form[1]/p[1]/button[1]/span[1]").click()




# agree to terms and conditions
driver.find_element_by_css_selector("#cgv").click()

# proceed to checkout
driver.find_element_by_xpath("//button[@name='processCarrier']//span[contains(text(),'Proceed to checkout')]").click()



# pay via bank wire
driver.find_element_by_xpath("//a[@class='bankwire']").click()


# confirm order
driver.find_element_by_xpath("//span[contains(text(),'I confirm my order')]").click()



# confirmation text
confirmation = driver.find_element_by_xpath("//strong[contains(text(),'Your order on My Store is complete.')]")
assert confirmation.text == 'Your order on My Store is complete.'

driver.quit()



