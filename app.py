pip install flash
pip install request
pip install beautifulsoup4

from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    products = scrape_products(url)
    return render_template('index.html', products=products)

def scrape_products(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    
    products = []
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if columns:
            item_name = columns[0].text.strip()
            item_price = columns[1].text.strip()
            item_description = columns[2].text.strip()
            
            product = {
                'name': item_name,
                'price': item_price,
                'description': item_description
            }
            
            products.append(product)
    
    return products

if __name__ == '__main__':
    app.run(debug=True)
