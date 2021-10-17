import re
import time
import os
from selenium import webdriver
from . import path

driver = webdriver.Chrome(executable_path=os.path.join(path, "chromedriver"))


def get_articles(term, pages=1, timeout=30):
    count = 101
    headlines = []
    for page in range(pages):
        if page * 100 >= count:
            break
        driver.get("https://www.cnn.com/search?size=100&q={}&from={}".format(term.replace(" ", "%20"), str(page * 100)))
        tries = 0
        headlines_temp = []
        while tries < timeout and not headlines_temp:
            tries += 1
            headlines_temp = driver.find_elements_by_class_name("cnn-search__result-headline")
            time.sleep(1)
        if headlines_temp:
            element = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[2]/div[2]/div/div[1]")
            count = int(re.findall(r"out of (\d+)", element.text)[0])
        headlines += [n.text for n in headlines_temp]
    return headlines
