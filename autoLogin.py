from selenium import webdriver
from getpass import getpass
import time

# username = input("Enter username : ")
# password = getpass("Your Password : ")
username = ""  #Letakkan Username disini
password = ""  #letakaan Password disini

driver = webdriver.Chrome("F:\\ProgramLanguage\\Python\\webdriver\\chromedriver.exe")

driver.get("https://lmsslc.polinema.ac.id/login/index.php")

username_textbox = driver.find_element_by_id("username")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(password)

login_button = driver.find_element_by_id("loginbtn")
login_button.submit()

time.sleep(2)
