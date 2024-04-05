import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("greynoise_api_key")

ip_address = "49.36.51.230"
url = "https://api.greynoise.io/v3/community/" + ip_address

headers = {
  'key': api_key
}

response = requests.request("GET", url, headers=headers)

print(response.text)