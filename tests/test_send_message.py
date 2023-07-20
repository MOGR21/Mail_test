import pathlib
from selenium import webdriver
from pathlib import Path

from pages.login_page import LoginPage
from pages.mail_page import MailPage


def test_send_message():

    dir_path = pathlib.Path.home()
    path = Path(dir_path, 'PycharmProjects', 'main_project_OODJI', 'utilities', 'chromedriver.exe')
    driver = webdriver.Chrome(path)

    print("Start Test Send Message")

    login = LoginPage(driver)
    login.open_login_page()
    login.autorization()

    sendmail = MailPage(driver)
    sendmail.send_letter()
    sendmail.get_screenshot()

    print("End Test Send Message")