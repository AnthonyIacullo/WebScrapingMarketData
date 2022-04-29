# Import the dependencies
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/trending-tickers'  # given url
page = requests.get(url)  # get request retrieves HTML data
soup = BeautifulSoup(page.text, 'lxml')  # lxml is the fastest parser

table = soup.find('table', class_='W(100%)')  # table for trending tickers data

# print(table)

# column headings
headers = []  # list to hold column headings of the table
for i in table.find_all('th')[0:8]:  # only gets 8 column headings
    heading_title = i.text.strip()  # gets heading title
    # print(heading_title)
    headers.append(heading_title)  # adds heading title to headers list

# print(headers)

df = pd.DataFrame(columns=headers)  # creates a dataframe with heading titles as columns

# get data from rows starting at the first row
for row in table.find_all('tr')[1:]:
    data = row.find_all('td')[0:8]  # only gets data from 8 columns
    # print(data)
    row_data = [td.text.strip() for td in data]  # separates data with commas to prep for being added to df
    # print(row_data)
    length = len(df)  # variable holds row number
    # print(length)
    df.loc[length] = row_data  # access a group of rows/columns by labels

df.to_csv('trendingtickers.csv')
