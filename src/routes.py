from flask import Blueprint, jsonify, request
import requests
from scrape import scrape

scrape_route = Blueprint('scrape_route', __name__)

@scrape_route.route('/scrape', methods=['POST'])
def scrape_handler():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'Missing url parameter.'}), 400

    try:
        result = scrape(url)
        return jsonify(result)

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

    except ValueError as e:
        return jsonify({'error': str(e)}), 500


catch_all = Blueprint('catch_all', __name__)

@catch_all.route('/', defaults={'path': ''})
@catch_all.route('/<path:path>')
def catch_all_handler(path):
    return jsonify({'message': 'Welcome to the lyrics API.'})
