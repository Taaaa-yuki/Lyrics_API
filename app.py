import re
import traceback
from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'Missing url parameter.'}), 400

    try:
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

        return jsonify(result)

    except requests.exceptions.RequestException as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

    except ValueError as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({'message': 'Welcome to the lyrics API.'})


if __name__ == '__main__':
    app.run(debug=True)
