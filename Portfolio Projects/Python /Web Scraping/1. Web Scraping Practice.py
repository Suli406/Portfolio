from bs4 import BeautifulSoup
import requests

def web_scraping_function():
    url = 'https://www.scrapethissite.com/pages/simple/'
    request = requests.get(url)
    content = BeautifulSoup(request.text, 'html.parser')
    print(content)

web_scraping_function()