''' this code demonstrates an end to end test automation execution '''

from selenium import webdriver
import time

#invoking webdriver
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

# maximizes the current window
driver.maximize_window()

driver.get("http://automationpractice.com/index.php")

# signing in 
driver.find_element_by_xpath("//a[@class='login']").click()

# enter email address
driver.find_element_by_css_selector("#email").send_keys("selormonray14@gmail.com")

# enter password
driver.find_element_by_css_selector("#passwd").send_keys("abcd1234")

driver.find_element_by_name("SubmitLogin").click()

driver.find_element_by_id("header_logo").click()

# buy faded short sleeves
# click on item
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/a[1]/img[1]").click()
# add to cart
driver.find_element_by_xpath("//span[contains(text(),'Add to cart')]").click()
# sleep for 4 seconds
time.sleep(4)
# continue shopping
driver.find_element_by_xpath("//span[@class='continue btn btn-default button exclusive-medium']//span[1]").click()
# go back to homepage
driver.find_element_by_id("header_logo").click()


# buy faded blouse
# click on item
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[2]/div[1]/div[1]/div[1]/a[1]/img[1]").click()
# add to cart
driver.find_element_by_xpath("//span[contains(text(),'Add to cart')]").click()
# sleep for 4 seconds
time.sleep(4)
# continue shopping
driver.find_element_by_xpath("//span[@class='continue btn btn-default button exclusive-medium']//span[1]").click()
# go back to homepage





driver.find_element_by_id("submit").submit()

driver.navigate()






# buy printed summer dress
# click on item
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[5]/div[1]/div[1]/div[1]/a[1]/img[1]").click()
# add to cart
driver.find_element_by_xpath("//span[contains(text(),'Add to cart')]").click()
# sleep for 4 seconds
time.sleep(4)
# proceed to check out
driver.find_element_by_xpath("//span[contains(text(),'Proceed to checkout')]").click()


# checkout
driver.find_element_by_xpath("//a[@class='button btn btn-default standard-checkout button-medium']//span[contains(text(),'Proceed to checkout')]").click()


driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/form[1]/p[1]/button[1]/span[1]").click()


# agree to terms and conditions
driver.find_element_by_css_selector("#cgv").click()
driver.find_element_by_xpath("//button[@name='processCarrier']//span[contains(text(),'Proceed to checkout')]").click()

# pay by bank wire
driver.find_element_by_xpath("//a[@class='bankwire']").click()

# confirm order
driver.find_element_by_xpath("//span[contains(text(),'I confirm my order')]").click()

# confirmation text
confirmation = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/p[1]/strong[1]")
assert confirmation.text == 'Your order on My Store is complete.'









driver.get_screenshot_as_png()


driver.current_url()








driver.quit()