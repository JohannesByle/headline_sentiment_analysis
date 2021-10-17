import pandas as pd
import urllib.request as request
from bs4 import BeautifulSoup
import certifi
import ssl
import json
from plots.headline_subset_bar import compare_subsets
import matplotlib.pyplot as plt
import numpy as np


def get_html(url):
    req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = request.urlopen(req, context=ssl.create_default_context(cafile=certifi.where()))
    return BeautifulSoup(response.read(), features="lxml")


with open("data/fox_governor_data.json", "r") as f:
    data = json.load(f)
headlines = []
for governor in data:
    headlines += data[governor]
headlines = np.unique(headlines)

r_govs = ["Ron DeSantis", "Greg Abbott", "Brian Kemp"]
d_govs = ["Phil Murphy", "Andrew Cuomo", "Michelle Lujan Grisham"]

compare_subsets(headlines, [n.split()[-1] for n in r_govs], [n.split()[-1] for n in d_govs])
plt.title("Fox Headlines")
plt.show()
