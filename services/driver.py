from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    def __init__(self):
        self.browser = None

    def start(self):
        chrome_options = Options()
        chrome_options.add_argument("--lang=en-US")
        chrome_options.add_argument("--window-size=800,800")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--no-sandbox")
        chrome_prefs = {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.notifications": 2
        }
        chrome_options.add_experimental_option("prefs", chrome_prefs)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.browser = webdriver.Chrome(options=chrome_options)

    def get_page(self, link):
        if not self.browser:
            raise Exception("Browser not started. Call 'start()' first.")

        self.browser.get(link)
        return self.browser

    def close(self):
        if self.browser:
            self.browser.quit()
