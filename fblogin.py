from selenium import webdriver
from getpass import getpass


username = int(input("Enter phone or email: "))
password = getpass("enter your password: ")



driver = webdriver.Firefox(executable_path="C:\\fire\\geckodriver.exe")

driver.get("https://www.facebook.com")

fb_userbox = driver.find_element_by_id("email") 
fb_userbox.send_keys(username)

fb_passbox = driver.find_element_by_id("pass")
fb_passbox.send_keys(password)
