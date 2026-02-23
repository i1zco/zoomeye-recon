from maltego_trx.transform import DiscoverableTransform
from maltego_trx.entities import IPv4Address
from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("ZOOMEYE")

class ZoomEyeDomain(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request, response):

        domain = request.Value
        page = 1 

        url = f"https://api.zoomeye.ai/domain/search?q={domain}&type=0&page={page}"

        headers = {
            "API-KEY": api_key
        }

        try:
            r = requests.get(url, headers=headers, verify=False)
            data = r.json()

            for item in data.get("list", []):
                ip = item.get("ip")
                name = item.get("name")
                time = item.get("timestamp")

                if ip:
                    ent = response.addEntity(IPv4Address, ip)
                    ent.addProperty("name", "Name", "strict", name if name else "")
                    ent.addProperty("time", "Time", "strict", str(time) if time else "")

        except Exception as e:
            response.addUIMessage(str(e))
