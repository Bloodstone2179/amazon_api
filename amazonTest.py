import requests




def requester(str):
    url = "http://127.0.0.1:5000/api/" + str
    page = requests.get(url=url)
    jsonPage = page.json()

    price = jsonPage["price"]
    productCode = jsonPage["Product Code"]
    name = jsonPage["name"] 
    urlRe = jsonPage["url"]
    return price, name,productCode,url
