from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

option = Options()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

driver = webdriver.Chrome()
driver.get("https://remarkablegames.org/button-clicker/")

# links = driver.find_elements("xpath", "//a[@href]")
# for link in links:
#     if "Books" in link.get_attribute("innerHTML"):
#         link.click()

link = driver.find_element(By.CSS_SELECTOR, "td[class='output-next']")
print(link)

link1 = driver.find_elements(By.XPATH, "//td[contains(@class, 'output-next ')]")
print(link1)
