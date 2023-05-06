import traceback
from flask import Flask, jsonify, request
import requests
from scrape import scrape

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape_route():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'Missing url parameter.'}), 400

    try:
        result = scrape(url)
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
