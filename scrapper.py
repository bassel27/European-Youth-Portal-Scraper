from re import sub
from ssl import OPENSSL_VERSION_NUMBER
from typing import KeysView, List
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement


class Scraper:
    def __init__(self):
        self.driver = None
        self.load_driver()
        self.wait = WebDriverWait(self.driver, WAIT_TIME)

    def load_driver(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=chrome_options
        )

    def fetch_url(self, url):
        self.driver.get(url)
        self.driver.page_source.encode("utf-8")

    def scroll_down_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_all_opps(self) -> List[WebElement]:
        return self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    OPP_XPATH,
                )
            )
        )

    def open_opp_in_new_tab(self, index):
        element = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"({OPP_XPATH})[{index+1}]",
                )
            )
        )
        href = element.get_attribute("href")
        self.driver.execute_script("window.open('%s', '_blank')" % href)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def accept_cookies(self):
        self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    ACCEPT_COOKIES_XPATH,
                )
            )
        )[1].click()
        self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    CLOSE_COOKIES_XPATH,
                )
            )
        )[1].click()

    def is_my_country_included(self):
        countries = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    COUNTRIES_XPATH,
                )
            )
        )
        return countries.text.__contains__(MY_COUNTRY)

    def get_opp_title(self):
        return self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    TITLE_XPATH,
                )
            )
        ).text

    def get_dates(self):
        return self.driver.find_element(By.XPATH, DATES_XPATH).text

    def get_location(self):
        return self.driver.find_element(By.XPATH, LOCATION_XPATH).text

    def get_deadline(self):
        return self.driver.find_element(By.XPATH, DEADLINE_XPATH).text

    def get_topics(self):
        elements = self.driver.find_elements(By.XPATH, TOPICS_XPATH)
        return [element.text for element in elements]

    def get_accommodation(self):
        return self.driver.execute_script(
            f"return document.evaluate('{ACCOMMODATION_XPATH}', document.body, null, XPathResult.STRING_TYPE).stringValue"
        )

    def get_description(self):
        return self.driver.execute_script(
            f"return document.evaluate('{DESCRIPTION_XPATH}', document.body, null, XPathResult.STRING_TYPE).stringValue"
        )
        

    def get_training(self):
        return self.driver.execute_script(
            f"return document.evaluate('{TRAINING_XPATH}', document.body, null, XPathResult.STRING_TYPE).stringValue"
        )

    def get_profile(self):
        return self.driver.execute_script(
            f"return document.evaluate('{PROFILE_XPATH}', document.body, null, XPathResult.STRING_TYPE).stringValue"
        )

    def get_current_url(self):
        return self.driver.current_url

    def load_more(self):
        self.driver.find_element(By.XPATH, LOAD_MORE_BUTTON_XPATH).click()
        
    def  close_current_tab(self):
        self.driver.close()

    def switch_to_main_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
