import requests
from Api import Weather_api_key

api_address = "http://api.openweathermap.org/data/2.5/forecast?id=1254361&appid=" + Weather_api_key

Data = requests.get(api_address).json()

print(api_address)
    