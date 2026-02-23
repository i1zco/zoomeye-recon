from maltego_trx.maltego import MaltegoMsg
import requests
import os
import sys
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ZOOMEYE")

domain = sys.argv[1]

url = f"https://api.zoomeye.ai/domain/search?q={domain}&type=0&page=1"

headers = {
    "API-KEY": API_KEY
}

response = requests.get(url, headers=headers)
data = response.json()

msg = MaltegoMsg()

for item in data.get("list", []):
    ip = item.get("ip")
    name = item.get("name")

    entity = msg.addEntity("maltego.IPv4Address", ip)
    entity.addProperty("label", "Name", "strict", name)

print(msg)
