import requests #loads the packages installed.

URL = "https://api.coingecko.com/api/v3/simple/price" #webaddress of CoinGecko free price API
params = {"ids": "bitcoin,ethereum", "vs_currencies": "gbp"} #tells the api what specifics you want so you dont pull it all.

response = requests.get(URL, params=params, timeout=10) #sends the request, timeout = 10 stops the program if coingecko doesnt respond in 10 seconds.
response.raise_for_status() #makes the program stop with clear error if the API returns a problem instead of carrying on with bad data.
data = response.json() #stores the JSON response in a variable

for coin, prices in data.items(): # loops through the data dictionary and unpacks the coin name and prices dictionary.
    print(f"{coin.title()}: £{prices['gbp']:,}")