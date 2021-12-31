#!/usr/bin/env python
# coding: utf-8

#Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

#Visit the Mars new site
url = 'https://redplanetscience.com'
browser.visit(url)

#Optional dealy for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

#Convert the browser html to asoup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div',class_='content_title')

#Use the parent element to find the first 'a' tage and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

#Use the parent element fto find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# ##JPL Space Images Featured IMage

#Visit URL
image_url = 'https://spaceimages-mars.com'
browser.visit(image_url)

#Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

#Parse the resulting html with souop
html = browser.html
img_soup = soup(html, 'html.parser')

#find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

#Use the base url to create and absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# ## Mars Facts Data Frame
mars_facts_df = pd.read_html('https://galaxyfacts-mars.com')[0]
mars_facts_df.columns = ['description', 'Mars', 'Earth']
mars_facts_df.set_index('description', inplace=True)
mars_facts_df

mars_facts_df.to_html()

browser.quit()

