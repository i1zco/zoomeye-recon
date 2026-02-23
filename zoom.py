import requests
import argparse
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ZOOMEYE")

def get_res(api_key, url):

   headers = {
         "API-KEY": api_key
   }
   resp = requests.get(url, headers=headers, verify=False)
   text = resp.json()
   results = []
   for item in text.get("list", []):
       results.append(f'Name: {item.get("name")}, IP: {item.get("ip")}, Time: {item.get("timestamp")}')
   return results


args = argparse.ArgumentParser()
args.add_argument("--domain", help="Enter Domain", required=True)
args.add_argument("--pages", type=int, default=1, help="Enter Len Pages")

arg = args.parse_args()
url = f"https://api.zoomeye.ai/domain/search?q={arg.domain}&type=0&page={arg.pages}"
result = get_res(api_key, url)
for i in result:
   print(i)

