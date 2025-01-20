import sys
import requests
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bank_site')
def bank_site():
    bank_site_content = requests.get('http://localhost:5000').content.decode()
    malicious_site_content = bank_site_content\
                                .replace('href="/', 'href="http://localhost:5000/')\
                                .replace('action="/', 'action="http://localhost:5000/')
    return malicious_site_content.encode()

if __name__ == "__main__":
    app.run(debug=True, port=8080)
