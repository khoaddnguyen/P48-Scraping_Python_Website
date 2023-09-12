from selenium import webdriver
from selenium.webdriver.common.by import By

WEBSITE_LINK = "https://www.python.org/"

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(WEBSITE_LINK)

# Search by CSS_SELECTOR
event_times = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
# for time in event_times:
#     print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
# for name in event_names:
#     print(name.text)

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }


# driver.close()  # close tab
driver.quit()  # quit entire browser
