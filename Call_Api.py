import requests
import json

url = "https://api.barcodespider.com/v1/lookup"

querystring = {"upc":"9781474821483"}

headers = {
    'token': "441d95fefd9720c9a560",
    'Host': "api.barcodespider.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "close",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring).text

parser = json.loads(response)

print(response)

#print(parser["item_attributes"]["upc"])

#python Call_Api.py

# shift + alt +f

