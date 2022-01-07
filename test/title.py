from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# SetUp & navigate to the home page
s = Service("/Users/kevinnestico/PycharmProjects/DemoCasino/drivers/chromedriver")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://demo.casino/")

# Click on sign in
locator_signIn_btn_xpath = "//header/div[1]/div[2]/div[2]/a[1]"
signIn_btn = driver.find_element(By.XPATH, locator_signIn_btn_xpath)
signIn_btn.click()

# Scroll down to "SIGN IN" btn
locator_signIn_btn = "//body/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/form[1]/fieldset[2]/button[1]"
element = driver.find_element(By.XPATH, locator_signIn_btn)
actions = ActionChains(driver)
actions.move_to_element(element).perform()

# Enter email/username
locator_email_id = "UserLogin_username"
email_txt_box = driver.find_element(By.ID, locator_email_id)
email_txt_box.send_keys("nesticokevin@gmail.com")

# Enter password
locator_password_id = "UserLogin_password"
password_txt = driver.find_element(By.ID, locator_password_id)
password_txt.send_keys("Test1010test")

# Click Sign-In btn
signIn_btn = driver.find_element(By.XPATH, locator_signIn_btn)
signIn_btn.click()

# Checks the title
actualTitle = driver.title
print(actualTitle)
title = "Demo Casino"
assert actualTitle == title, "The title does not match"

# Close
driver.close()
driver.quit()
