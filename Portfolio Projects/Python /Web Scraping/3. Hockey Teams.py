from bs4 import BeautifulSoup
import requests
from urllib3 import request

url = 'https://www.scrapethissite.com/pages/forms/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# The main table we're using to extract data from

table = soup.find_all('table', class_ = 'table')

# To find the headers/columns for our dataframe

clean_headers = []
for header in table:
    full_header = header.find_all('tr')[0]
    individual_headers = full_header.find_all('th')
    clean_headers = [title.text.strip() for title in individual_headers]
    break

# To find all the individual rows of data from the table

clean_rows = []
for data in table:
    all_rows = data.find_all('tr')[1:]
    for all_data in all_rows:
        individual_data = all_data.find_all('td')
        clean_data = [cell.text.strip() for cell in individual_data]
        clean_rows.append(clean_data)

import pandas as pd

df = pd.DataFrame(clean_rows, columns=clean_headers)
print(df)