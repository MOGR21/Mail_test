from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Base.base_class import Base


class MailPage(Base):

    # Locators

    button_send_message = "//span[@class='compose-button__txt']"
    to_whom = "(//input[@class='container--H9L5q size_s--3_M-_'])[1]"
    letter_subject = "(//input[@class='container--H9L5q size_s--3_M-_'])[2]"
    send_button = "(//span[@class='vkuiButton__in'])[1]"
    text_input = "//div[@role='textbox']"

    # Getters

    def get_button_send_message(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_send_message)))

    def get_to_whom(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.to_whom)))

    def get_letter_subject(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.letter_subject)))

    def get_send_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.send_button)))

    def get_text_input(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.text_input)))

    # Actions

    def click_button_send_message(self,):
        self.get_button_send_message().click()
        print("Click Button Send Message")

    def input_to_whom(self, mail_name):
        self.get_to_whom().send_keys(mail_name)
        print("Input To Whom")

    def input_letter_subject(self, subject):
        self.get_letter_subject().send_keys(subject)
        print("Input Letter Subject")

    def input_text_input(self, text):
        self.get_text_input().send_keys(text)
        print("Input Text")

    def click_send_button(self, ):
        self.get_send_button().click()
        print("Click Send Button")

    # Methods

    def send_letter(self):
        self.click_button_send_message()
        self.input_to_whom("test_mogr@mail.ru")
        self.input_letter_subject("Ну привет!!!")
        self.input_text_input("Привет самому себе!!!!")
        self.click_send_button()
        sleep(5)
