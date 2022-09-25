from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import selenium as sl


account = input("Do You Want To Create A New Account or log in : ")


# importing The Path Of The WebDriver
path = "/home/ammar/Downloads/chromedriver"

driver = webdriver.Chrome(path)

actions = ActionChains(driver)

# Wich Website Do I Want To Go To
driver.get("https://www.amazon.com/ref=nav_logo")


def new_account():

    if account == " Create A New Account" or account == "c" or account == 'C':

        name = input("What Is Your Name: ")

        mobile_num = input("What Is Your Mobile Number or Your Email: ")

        while True:
            password = input("What is your Password: ")
            if len(password) < 6:
                print("Password Has To Be More Than 6 charecters long")
                continue
            else:
                break
        # Waiting 0.1 Seconds
        time.sleep(0.1)

        hello = driver.find_element_by_id("nav-link-accountList-nav-line-1")

        hello.click()

        # Waiting 0.1 Seconds
        time.sleep(0.1)

        new_account = driver.find_element_by_id("createAccountSubmit")

        new_account.click()

        First_Name = driver.find_element_by_id("ap_customer_name")

        Mob_or_email = driver.find_element_by_id("ap_email")

        Passwo = driver.find_element_by_id("ap_password")

        re_enter_pass = driver.find_element_by_id("ap_password_check")

        verify_email = driver.find_element_by_id("continue")

        First_Name.send_keys(name)

        Mob_or_email.send_keys(mobile_num)

        Passwo.send_keys(password)

        re_enter_pass.send_keys(password)

        verify_email.click()

        print("You Have To Verify Your Mobile Number or Your Email and Then Your Account Is Created")


def login():
    if account == "log in" or account == "login":

        Email = input("What is your email: ")

        password = input("What Is Your Password:   ")

        # Waiting 0.1 Seconds
        time.sleep(0.1)

        hello = driver.find_element_by_id("nav-link-accountList-nav-line-1")

        hello.click()
        # Waiting 0.1 Seconds

        time.sleep(0.1)

        Adding_Email = driver.find_element_by_id("ap_email")

        Adding_Email.send_keys(Email)

        con = driver.find_element_by_id("continue")

        con.click()

        Adding_Password = driver.find_element_by_id("ap_password")

        Adding_Password.send_keys(password)

        sign_in = driver.find_element_by_id("signInSubmit")

        sign_in.click()

        print("A Verfication Code Has Been Sent To You ")


new_account()
login()
