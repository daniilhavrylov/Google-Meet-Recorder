import os
import time

from dotenv import load_dotenv
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from services.audio import record
from services.driver import Driver

load_dotenv()

def data_tooltip_click(browser, key_word):
    css_element = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f"[data-tooltip*='{key_word}']"))
    )
    css_element.click()

def check_join(browser):
    try:
        join_button = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Join now']]"))
        )
        join_button.click()
        return True
    except(TimeoutException, NoSuchElementException):
        return False

def end_detection(browser):
    while True:
        imgs = browser.find_elements(By.CSS_SELECTOR, "img.SOQwsf")
        if len(imgs) < 2:
            break
        time.sleep(2)

def connect_bot(driver: Driver):
    invite_link = os.getenv('INVITE_LINK')
    bot_name = os.getenv('BOT_NAME')

    browser = driver.get_page("https://google.com")
    time.sleep(2)
    browser.get(invite_link)

    webdriver_status = browser.execute_script("return navigator.webdriver")
    if not webdriver_status:
        time.sleep(5)
        input_field = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
        )
        input_field.clear()
        input_field.send_keys(bot_name)

        data_tooltip_click(browser, 'camera')
        data_tooltip_click(browser, 'microphone')
        time.sleep(5)
        if check_join(browser):
            # record()
            time.sleep(5)
        end_detection(browser)

def main():
    driver = Driver()
    try:
        driver.start()
        connect_bot(driver)
    finally:
        driver.close()


if __name__ == "__main__":
    main()