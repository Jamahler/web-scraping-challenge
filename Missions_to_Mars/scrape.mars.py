from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    executable_path = {'executable_path': 'C:/Users/jamah/OneDrive/Desktop/GT Boot Camp/Downloads/chromedriver'} 
    browser = Browser('chrome', **executable_path, headless=False)

def scrape_info():
    url = "https://mars.nasa.gov/news"
    browser.visit(url)

    url = "https://mars.nasa.gov/news"
    browser.visit(url)

