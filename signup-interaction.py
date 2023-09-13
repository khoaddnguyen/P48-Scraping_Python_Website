from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SIGNUP_PAGE = "http://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(SIGNUP_PAGE)

# type into search bar
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("My First Name")
first_name.send_keys(Keys.TAB)
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("My Last Name")
email = driver.find_element(By.NAME, "email")
email.send_keys("myemail@email.com")
button = driver.find_element(By.CSS_SELECTOR, value="button")
button.click()

# driver.quit()  # quit entire browser
