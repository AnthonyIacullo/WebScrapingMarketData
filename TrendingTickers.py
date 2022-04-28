# Import the dependencies
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/trending-tickers'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table', class_='W(100%)')

print(table)

headers = []

for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)

print(headers)

df = pd.DataFrame(columns=headers)

for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data

df.to_csv('chc.csv')
