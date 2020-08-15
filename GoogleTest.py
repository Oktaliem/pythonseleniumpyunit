from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
driver.implicitly_wait(30000)
print(driver.current_url)
# driver.quit()
