from flask import Flask

import scraper

app = Flask(__name__)

@app.route('/')
def index():
    return 'Server Works!'
  
@app.route('/scrape/<ticker>')
def scrape_url(ticker):
    text = scraper.scrape_url(ticker, 'http://wilsoninformatics.com')
    return 'Paragraph: %s' % text