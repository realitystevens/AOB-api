import os
import requests
from decouple import config


url = "https://127.0.0.1:8000/api/products/"

API_TOKEN = config('API_TOKEN') or os.environ.get('API_TOKEN')

headers = {
    "Content-Type": "application/json",
    "Authorization" : "Token f{API_TOKEN}"
}


response = requests.get(url, headers=headers)

print(response.json())