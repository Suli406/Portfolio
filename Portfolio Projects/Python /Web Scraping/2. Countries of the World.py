from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/simple/'
request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')


all_countries = soup.find_all('div', class_ = 'col-md-4 country') # find_all returns a list

for country in all_countries:
    individual_country = country.find('h3')
    print(individual_country.text.strip())

