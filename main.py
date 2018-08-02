import os

import requests
from flask import Flask, send_file, Response, redirect
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def post_pig(fact):
	response = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/", data = {'input_text': fact}, allow_redirects = False)
	header_url = response.headers['Location']
	return header_url


@app.route('/')
def home():
    fact = get_fact().strip()
    pig = post_pig(fact)
    return redirect(pig)




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

