# Import the required modules
from selenium import webdriver
import time

from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
import os
from dotenv import load_dotenv
from pathlib import Path

from Change_Sheet_Name import change_sheet_name


# Main Function


def get_niid_spool(start_date,end_date,SHOW_WINDOW,LINK):
    #enviroment variables
    load_dotenv()
    THIRD_PARTY_PLATFORM_LINK = os.getenv("3RD_PARTY_PLATFORM_LINK")
    THIRD_PARTY_PLATFORM_EMAIL = os.getenv("3RD_PARTY_PLATFORM_EMAIL")
    THIRD_PARTY_PLATFORM_PASSWORD = os.getenv("3RD_PARTY_PLATFORM_PASSWORD")

    # download path
    downloads_path = Path.home() / "Downloads"
    directory_path = downloads_path
    file_name = "NIID Spool.xlsx"
    file_path = os.path.join(directory_path, file_name)

    # Provide the email and password
    email = LINK[1]
    password = THIRD_PARTY_PLATFORM_PASSWORD

    #wait time
    wait_time = 0


    # start_date = "01-Sep-2023"
    # end_date = "30-Sep-2023"

    # driverService = webdriver.ChromeService
    # driverService.HideCommandPromptWindow = True;

    options = webdriver.ChromeOptions()
    options.add_argument(SHOW_WINDOW)
    # options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--no-sandbox")  # Required if running on certain environments
    options.add_argument("--disable-extensions")  # Disable extensions in headless mode
    options.add_argument("--window-size=1920x1080")  # Set window size to ensure proper rendering
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--log-level=0')

    # Provide the path of chromedriver present on your system.
    path = (r"chromedriver.exe")
    service = Service(executable_path=path)
    service.creation_flags = 0x08000000
    driver = webdriver.Chrome(options=options, service=service)
    driver.set_window_size(1920, 1000)
    # driver.minimize_window()

    try:
        # Send a get request to the url
        driver.get(LINK[0])
        time.sleep(0.2)
        # https: // auth.geeksforgeeks.org /

        # Finds the input box by name in DOM tree to send both
        # the provided email and password in it.
        username = driver.find_element(by="xpath",
                                       value='//div[@class="col-md-offset-2 col-md-4 center-block panel-primary"]/input[1]')
        username.send_keys(email)
        keycode = driver.find_element(by="xpath",
                                      value='//div[@class="col-md-offset-2 col-md-4 center-block panel-primary"]/input[2]')
        keycode.send_keys(password)

        # Find the signin button and click on it.
        driver.find_element(by="xpath", value='//div/input[3]').click()
        time.sleep(0.2)

        # Find the Utility  button and click on it.
        driver.find_element(
            by="xpath", value='//div[@class="menu-list"]/ul/ul/div[6]/div/li/a').click()
        time.sleep(0.5)

        # Find the Update Policy button and click on it.
        driver.find_element(
            by="xpath", value='//div[@class="menu-list"]/ul/ul/div[6]/div[2]/ul/li[3]').click()
        time.sleep(0.5)

        # Find the Search by option and click on it.
        driver.find_element(
            by="xpath",
            value='//div[@class="col-md-12"]/select').click()
        time.sleep(0.2)

        # Find the fetch by policy button and click on it.
        driver.find_element(
            by="xpath",
            value='//div[@class="col-md-12"]/select/option[5]').click()
        time.sleep(0.5)

        # Finds the input box by name in DOM tree to send
        # the provided start date to it
        policy_number = driver.find_element(
            by="xpath",
            value='//div[@class="row"][3]/div/input')
        policy_number.send_keys(start_date)
        time.sleep(0.5)
        # Finds the input box by name in DOM tree to send
        # the provided end date to it
        policy_number = driver.find_element(
            by="xpath",
            value='//div[@class="row"][3]/div[2]/input')
        policy_number.send_keys(end_date)
        time.sleep(0.5)

        # Find the Spool button and click on it.
        driver.find_element(
            by="xpath",
            value='//div[@class="row"][4]/input').click()
        time.sleep(2)

        try:
            while not os.path.isfile(file_path) and wait_time <= 50:
                time.sleep(5)
                wait_time += 1
                print(f"The file '{file_name}' does not exists in the directory '{directory_path}'.")
                print(wait_time)
        except Exception as e:
            print(e)

        time.sleep(5)
    except WebDriverException:
        print("Browser window was closed by the user.")


