from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# link = "http://suninjuly.github.io/registration1.html"

try:
    print("Wait for browser to open...")
    browser = webdriver.Chrome()

    for link in ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]:
        print(f"Testing link {link}")
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
        input3.send_keys("pochta@mail.com")
        input4 = browser.find_element(By.CSS_SELECTOR, ".second_block input.first")
        input4.send_keys("88005553535")
        input5 = browser.find_element(By.CSS_SELECTOR, ".second_block input.second")
        input5.send_keys("kakoi-to adress")
        button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
        button.click()

        print("Success!")

except Exception as e:
    print(f"Failed: Got exception: {e}")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()