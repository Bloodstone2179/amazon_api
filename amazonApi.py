from flask import *
import json
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

#variables
name = str()
price = str()
code = str()

@app.route('/api/<product_code>')#, methods=['GET'])#
def api(product_code):
    global name, price,code
    code = product_code
    page = requests.get("https://www.amazon.co.uk/dp/" + code ,headers={"User-Agent":"Defined"})
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find("span", {"class": "a-offscreen"})
    name = soup.find("span", {"class": "a-size-large product-title-word-break"})
    nameText = name.get_text()
    priceText = price.get_text()
    print(price)
    json_raw = {
        "name":  nameText,  
        "price": priceText, 
        "Product Code": code,
        "url": page.url
    }
    return jsonify(json_raw)
