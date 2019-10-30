from selenium import webdriver as wd
import time
import requests as req
from bs4 import BeautifulSoup
import time
import urllib3.request
from contextlib import closing

from urls_and_xpaths import *
from parse_html import *

index = 0
for url in all_urls:
  browser = wd.Chrome(r"C:\Users\cemal\Downloads\chromedriver_win32\chromedriver.exe")
  browser.get(url)
  for xpath in all_xpaths[index]:
    button = browser.find_element_by_xpath(xpath)
    button.click()
    time.sleep(4)
    raw_htmls.append(browser.page_source)
  browser.close()
  parseHtml(raw_htmls, index)
  raw_htmls = []
  index += 1
