import re
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request
import requests
import traceback


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/scrape", methods=["POST", "GET"])
def scrape():
    if request.method == "POST":
        url = request.form.get("url")
        try:
            html = requests.get(url).text
            soup = BeautifulSoup(html, "html.parser")

            title = soup.find("h2", class_="ms-2 ms-md-3").text.strip()
            artist = soup.find("span", itemprop="byArtist name").text.strip()
            body = soup.find("div", id="kashi_area").prettify()
            body = re.sub(r"\s*<br\s*/?>\s*", "\n", body).strip()
            body = BeautifulSoup(body, "html.parser").text.strip()


            result = {
                "title": title,
                "artist": artist,
                "body": body
            }

            return jsonify(result)
        except:
            # traceback.print_exc()
            # return jsonify({"error": str(e)})
            return jsonify({"error": "Failed to scrape body."})
    elif request.method == "GET":
        return "Please make a POST request to /scrape with the 'url' parameter."

if __name__ == "__main__":
    app.run(debug=True)