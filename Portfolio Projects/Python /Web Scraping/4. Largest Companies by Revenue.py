from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

clean_columns = []
table = soup.find_all('table')[0]
header = table.find_all('tr')[0]
titles = header.find_all('th')
clean_titles = [clean.text.strip() for clean in titles]
clean_columns.append(clean_titles)

clean_rows = []
all_rows = table.find_all('tr')[1:]
for data in all_rows:
    individual_data = data.find_all('td')
    clean_data = [clean_datas.text.strip() for clean_datas in individual_data]
    clean_rows.append(clean_data)


import pandas as pd
df = pd.DataFrame(clean_rows, columns = clean_columns)
print(df)

