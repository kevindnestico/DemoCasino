from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

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

# Click buy credit btn
locator_buyCredit_btn_class = "header-user__transactions"
buyCredit_btn= driver.find_element(By.CLASS_NAME, locator_buyCredit_btn_class)
buyCredit_btn.click()

# Click deposit btn
locator_deposit_btn_xpath = "//body/div[1]/main[1]/div[1]/section[1]/section[1]/div[1]/ul[1]/li[1]/a[1]"
deposit_btn = driver.find_element(By.XPATH, locator_deposit_btn_xpath)
deposit_btn.click()

# Enter amount
locator_amount_id = "DepositForm_amount"
amount_txt = driver.find_element(By.ID, locator_amount_id)
amount_txt.send_keys("50")

# Click 2nd deposit btn
locator_2nd_deposit_btn_id = "btn-deposit"
deposit_btn = driver.find_element(By.ID, locator_2nd_deposit_btn_id)
deposit_btn.click()

# Sleep to check the result visually.
time.sleep(5)

# Close
driver.close()
driver.quit()
