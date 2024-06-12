import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ContactManagerTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver', options=options)
        self.driver.get("http://127.0.0.1:5000")  # Убедитесь, что порт совпадает с вашим приложением

    def tearDown(self):
        self.driver.quit()

    def test_load_main_page(self):
        driver = self.driver
        self.assertIn("Contact Manager", driver.title)

    def test_add_contact(self):
        driver = self.driver
        name_input = driver.find_element(By.ID, "name")
        phone_input = driver.find_element(By.ID, "phone")
        add_button = driver.find_element(By.XPATH, "//button[text()='Add']")

        name_input.send_keys("John Doe")
        phone_input.send_keys("123-456-7890")
        add_button.click()

        time.sleep(1)  # Ждем, чтобы обновился список контактов

        contacts = driver.find_elements(By.CSS_SELECTOR, "#contacts li")
        self.assertTrue(any("John Doe - 123-456-7890" in contact.text for contact in contacts))

    def test_delete_contact(self):
        driver = self.driver

        # Добавляем контакт перед удалением
        name_input = driver.find_element(By.ID, "name")
        phone_input = driver.find_element(By.ID, "phone")
        add_button = driver.find_element(By.XPATH, "//button[text()='Add']")

        name_input.send_keys("Jane Doe")
        phone_input.send_keys("098-765-4321")
        add_button.click()

        time.sleep(1)  # Ждем, чтобы обновился список контактов

        contacts = driver.find_elements(By.CSS_SELECTOR, "#contacts li")
        delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

        self.assertTrue(any("Jane Doe - 098-765-4321" in contact.text for contact in contacts))

        # Удаляем контакт
        for contact, delete_button in zip(contacts, delete_buttons):
            if "Jane Doe - 098-765-4321" in contact.text:
                delete_button.click()
                break

        time.sleep(1)  # Ждем, чтобы обновился список контактов

        contacts = driver.find_elements(By.CSS_SELECTOR, "#contacts li")
        self.assertFalse(any("Jane Doe - 098-765-4321" in contact.text for contact in contacts))

if __name__ == "__main__":
    unittest.main()
