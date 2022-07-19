import requests
city_name = "Osh"
API_key = '48f56f7b62a5c368126ca352e69f0fac'
API_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
response = requests.get(API_url)
print(response)