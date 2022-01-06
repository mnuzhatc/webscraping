import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/nuzhat/Documents/CIS 403/Week 18/chromedriver')
driver.get('https://glossedbyfay.com/collections/shop-glosses')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, features='html.parser')

driver.quit()

# Gets the product names
for a in soup.find_all(attrs='card__info'):
    names = a.find('h3')
    if names not in results:
        results.append(names.text)

# Gets the prices correlating with product name
for b in soup.find_all(attrs='card__price'):
    summary = b.find('span')
    if summary not in results:
        other_results.append(summary.text)

# Accounts for one item that has no price
other_results.insert(2, 'Sold Out')

# Organizes data into file
df = pd.DataFrame({'Makeup Item': results , ' Price': other_results})
df.to_csv('titles.csv', index=False, encoding='utf-8')
