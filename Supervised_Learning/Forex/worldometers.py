import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class Worldometers:
    def __init__(self):
        pass

    # ok
    def get_us_population_live(self=None):
        us_population_live = 0

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='geckodriver.exe', options=options)

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.worldometers.info/world-population/us-population/')

        time.sleep(10)

        element = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div/div[1]/div")

        if element is not None:
            us_population_live += float(element.text.replace(",", ""))

        browser.close()

        return us_population_live
