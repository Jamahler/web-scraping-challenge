from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

def init_browser():
    executable_path = {'executable_path': 'C:/Users/jamah/OneDrive/Desktop/GT Boot Camp/Downloads/chromedriver'} 
    return Browser('chrome', **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    mars_data = {}

    url = "https://mars.nasa.gov/news"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    mars_data["news_title"] = soup.find("div", class_="content_title").get_text()
    mars_data["news_p"] = soup.find("div", class_="description").get_text()

    url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_img)


