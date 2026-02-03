from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.bing.com/")

search_box = driver.find_element(By.ID, "sb_form_q")
search_box.send_keys("Ingenieria de Software UAZ")
sleep(2)
search_box.send_keys(Keys.RETURN)
sleep(5)

results = driver.find_elements(By.TAG_NAME, "h2")
for result in results:
    print(result.text)

driver.quit()
