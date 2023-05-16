import time
from selenium.webdriver.common.by import By
from main import driver

driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "login-otp-button").click()
driver.find_element(By.CSS_SELECTOR, "#messages-button > .badge").click()
driver.find_element(By.ID, "new-message-btn").click()
driver.find_element(By.NAME, "message.topicName").click()
time.sleep(5)
dropdown = driver.find_element(By.NAME, "message.topicName")
dropdown.find_element(By.XPATH, "//option[. = 'Прочее']").click()
time.sleep(5)
driver.find_element(By.NAME, "message.text").click()
driver.find_element(By.NAME, "message.text").send_keys("Отправка сообщения с типом - прочее")
time.sleep(5)
driver.find_element(By.ID, "send-button").click()
driver.close()

