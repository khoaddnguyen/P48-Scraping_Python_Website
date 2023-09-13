from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

WIKI_LINK = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(WIKI_LINK)

# click via CSS Locator
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# click via text search
comm_portals = driver.find_element(By.LINK_TEXT, "Community portal")
# comm_portals.click()

# type into search bar
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.quit()  # quit entire browser