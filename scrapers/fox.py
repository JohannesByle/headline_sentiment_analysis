import os
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from . import path
import time

driver = webdriver.Chrome(executable_path=os.path.join(path, "chromedriver"))


def get_articles(term):
    driver.get("https://www.foxnews.com/search-results/search?q={}".format(term.replace(" ", "%20")))
    load_more = True
    while load_more:
        try:
            time.sleep(2)
            driver.find_element_by_class_name("load-more").find_element_by_css_selector("a").click()
        except ElementNotInteractableException:
            load_more = False
    headlines = [n.text for n in driver.find_elements_by_class_name("title")]
    return headlines[2:]
