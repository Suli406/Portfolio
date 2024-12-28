import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.pastic.gov.pk/database-overseas-investors.aspx'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)
table = soup.find_all('table')[1]
#print(table)

clean_headers = []
full_headers = table.find_all('tr')[0]
individual_headers = full_headers.find_all('th')
clean_individual_headers = [clean.text.strip() for clean in individual_headers]
clean_headers.append(clean_individual_headers)
print(clean_headers)

clean_data = []
all_data = table.find_all('tr')
for data in all_data:
    individual_data = data.find_all('td')
    clean_row = [clean.text.strip() for clean in individual_data]
    clean_row.append(clean_data)