from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Base.base_class import Base


class LoginPage(Base):

    url = "https://account.mail.ru/login?&fail=1&from=navi"

    # Locators

    input_name = "//input[@name='username']"
    button_password = "//button[@data-test-id='next-button']"
    input_password = "//input[@name='password']"
    submit_button = "//button[@data-test-id='submit-button']"

    # Getters

    def get_input_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_name)))

    def get_button_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_password)))

    def get_input_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_password)))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.submit_button)))

    # Actions

    def input_user_name(self, mail_name):
        self.get_input_name().click()
        self.get_input_name().send_keys(mail_name)
        print("Input User Name")

    def click_button_password(self,):
        self.get_button_password().click()
        print("Click Button Password")

    def input_input_password(self, user_password):
        self.get_input_password().send_keys(user_password)
        print("Input User Password")

    def click_submit_button(self, ):
        self.get_submit_button().click()
        print("Click Submit Button")

    # Methods

    def open_login_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()

    def autorization(self):
        self.input_user_name("test_mogr")
        self.click_button_password()
        self.input_input_password("Ntcn1818")
        self.click_submit_button()
        sleep(5)

