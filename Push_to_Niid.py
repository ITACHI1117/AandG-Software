from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os
from pathlib import Path


def Push_to_Niid(SHOW_WINDOW):
    load_dotenv()
    NIID_EMAIL = os.getenv("NIID_EMAIL")
    NIID_PASSWORD = os.getenv("NIID_PASSWORD")
    NIID_LINK = os.getenv("NIID_LINK")

    # Provide the email and password
    email = NIID_EMAIL
    password = NIID_PASSWORD
    comapny_email = 'info@aginsuranceplc.com'

    # Downaload path
    downloads_path = Path.home() / "Downloads"
    file_path = f"{downloads_path}/NIID Spool.xlsx"

    # Driver options
    options = webdriver.ChromeOptions()
    options.add_argument(SHOW_WINDOW)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--start-minimized")
    options.add_argument('--log-level=0')

    # Provide the path of chromedriver present on your system.
    path = (r"chromedriver.exe")
    service = Service(executable_path=path)
    service.creation_flags = 0x08000000
    driver = webdriver.Chrome(options=options, service=service)
    # driver.set_window_size(1920, 1080)

    # Send a get request to the url
    driver.get(NIID_LINK)
    time.sleep(0.2)
    # Finds the input box by name in DOM tree to send both
    # the provided email and password in it.
    username = driver.find_element(by="xpath",
                                   value='//div[@id="MainContent_UpdatePanel1"]/table/tbody/tr[2]/td[2]/span/input')
    username.send_keys(email)
    keycode = driver.find_element(by="xpath",
                                  value='//input[@class="riTextBox riEnabled Textbox_Large"]')
    keycode.send_keys(password)
    time.sleep(0.8)

    # Find the Login button and click on it.
    driver.find_element(
        by="xpath", value='//div[@id="MainContent_UpdatePanel1"]/table/tbody/tr[7]/td/a/input').click()
    time.sleep(0.8)

    # Find upload button and click on it
    driver.find_element(by="xpath", value='//form/table/tbody/tr[5]/td[2]/div/div/a[2]').click()
    time.sleep(0.8)

    # Checking for the alert and clicking on it
    alert = driver.switch_to.alert
    alert.accept()

    # Find select button and click on it
    driver.find_element(by="xpath", value='//form/table/tbody/tr[7]/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr[6]/td/table/tbody/tr[4]/td[2]/select').click()
    time.sleep(0.8)

    # Find select button and click on it
    driver.find_element(by="xpath",
                        value='//form/table/tbody/tr[7]/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr[6]/td/table/tbody/tr[4]/td[2]/select/option[2]').click()
    time.sleep(0.8)


    #Uploading the file
    time.sleep(0.8)
    driver.find_element(by="xpath", value="//form/table/tbody/tr[7]/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr[7]/td[2]/div/ul/li/span/input[3]").send_keys(file_path)
    time.sleep(10)

    #Upload button
    driver.find_element(by="xpath", value="//form/table/tbody/tr[7]/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr[9]/TD[2]/span/input").click()
    cssValue = driver.find_element(
        by="xpath", value='//div[@id="MainContent_UpdateProgress1"]').value_of_css_property('display')
    print(cssValue)

    while cssValue == 'block':
        cssValue = driver.find_element(
            by="xpath", value='//div[@id="MainContent_UpdateProgress1"]').value_of_css_property('display')
        print(cssValue)
        print('Loading...')
        time.sleep(5)
        if cssValue == 'none':
            print("Done Loading✅")

    errmessage = driver.find_element(by="xpath", value='//span[@id="MainContent_lblErrorMessage"]')
    time.sleep(2)
    return errmessage.text





