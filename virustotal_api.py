import requests
from dotenv import load_dotenv
import os
load_dotenv()

ip_address = "49.36.51.230"
url = "https://www.virustotal.com/api/v3/ip_addresses/" + ip_address

api_key = os.getenv("virustotal_api_key")

headers = {
    "accept": "application/json",
    "x-apikey": api_key
}

response = requests.get(url, headers=headers)

print(response.text)