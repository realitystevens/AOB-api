import os
import requests
from decouple import config



BASE_URL = config('BASE_URL') or os.environ.get('BASE_URL')
API_TOKEN = config('API_TOKEN') or os.environ.get('API_TOKEN')

url = f"{BASE_URL}/api/products/"

headers = {
    "Content-Type": "application/json",
    "Authorization" : "Token f{API_TOKEN}"
}


response = requests.get(url, headers=headers)

print(response.json())
