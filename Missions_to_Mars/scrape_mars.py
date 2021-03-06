from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

def init_browser():
    executable_path = {"executable_path": "C:/Users/jamah/OneDrive/Desktop/GT Boot Camp/Downloads/chromedriver"} 
    return Browser('chrome', **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    mars_data = {}

    url = "https://mars.nasa.gov/news"
    browser.visit(url)

    time.sleep(10)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    mars_data["news_title"] = soup.find("div", class_="content_title").get_text()
    mars_data["news_p"] = soup.find("div", class_="description").get_text()

    url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_img)

    time.sleep(10)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    img = soup.find("img", class_='thumb')["src"]
    mars_data["featured_image_url"] = "https://www.jpl.nasa.gov" + img

    url_table = "https://space-facts.com/mars"

    time.sleep(10)

    mars_table = pd.read_html(url_table)
    mars_df = mars_table[0]
    mars_df.columns = ["Facts", "Data"]
    mars_df = mars_df.to_html()
    mars_data["mars_df"] = mars_df.replace('\n','')

    img_urls = []

    cerberus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(cerberus_url)

    time.sleep(10)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    cerberus_img = soup.find("img", class_="wide-image")["src"]
    cerberus_title = soup.find("h2", class_="title").get_text()
    cerberus_img_url = cerberus_url + cerberus_img
    cerberus = {"title": cerberus_title, "img_url": cerberus_img_url}
    img_urls.append(cerberus)

    schiaparelli_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(schiaparelli_url)

    time.sleep(10)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    schiaparelli_img = soup.find("img", class_="wide-image")["src"]
    schiaparelli_title = soup.find("h2", class_="title").get_text()
    schiaparelli_img_url = schiaparelli_url + schiaparelli_img
    schiaparelli = {"title": schiaparelli_title, "img_url": schiaparelli_img_url}
    img_urls.append(schiaparelli)

    syrtis_major_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(syrtis_major_url)

    time.sleep(10)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    syrtis_major_img = soup.find("img", class_="wide-image")["src"]
    syrtis_major_title = soup.find("h2", class_="title").get_text()
    syrtis_major_img_url = syrtis_major_url + syrtis_major_img
    syrtis_major = {"title": syrtis_major_title, "img_url": syrtis_major_img_url}
    img_urls.append(syrtis_major)

    valles_marineris_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(valles_marineris_url)

    time.sleep(10)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    valles_marineris_img = soup.find("img", class_="wide-image")["src"]
    valles_marineris_title = soup.find("h2", class_="title").get_text()
    valles_marineris_img_url = valles_marineris_url + valles_marineris_img
    valles_marineris = {"title": valles_marineris_title, "img_url": valles_marineris_img_url}
    img_urls.append(valles_marineris)

    mars_data["img_urls"] = img_urls

    browser.quit()

    return mars_data

    


    









