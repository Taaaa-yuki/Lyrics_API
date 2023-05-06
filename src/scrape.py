import re
from bs4 import BeautifulSoup
import requests

def scrape(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('h2', class_='ms-2 ms-md-3').text.strip()
    artist = soup.find('span', itemprop='byArtist name').text.strip()
    body = soup.find('div', id='kashi_area')
    if not body:
        raise ValueError('Failed to find kashi_area div.')
    body = re.sub(r'\s*<br\s*/?>\s*', '\n', str(body)).strip()
    body = BeautifulSoup(body, 'html.parser').text.strip()

    result = {
        'title': title,
        'artist': artist,
        'body': body
    }

    return result
