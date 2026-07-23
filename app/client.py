import httpx
import re
import json

from app.config import BASE_URL

# Paste your browser session cookie here
SESSION_COOKIE = "__Secure-better-auth.session_token=aHRPCYOvYx2fMoVv9deqgfQzJQpLyOy4.138X1u58DrGELtyUodSYMUkQ7%2Fl%2FrLXseoLJo5HihAs%3D"


class UrjaPortalClient:
    def __init__(self):
        self.client = httpx.Client(
            base_url=BASE_URL,
            follow_redirects=True,
            headers={
                "Cookie": SESSION_COOKIE,
                "User-Agent": "Mozilla/5.0",
                "Accept": "text/html,application/json"
            }
        )

    def login(self):
        return True

    def get_meters(self, page=1):
        response = self.client.get(
            "/portal/meters/search",
            params={
                "q": "",
                "page": page
            }
        )

        response.raise_for_status()
        return response.json()

    def get_meter_details(self, meter_id):
        import re
        import json
        from bs4 import BeautifulSoup

        response = self.client.get(f"/meters/{meter_id}")
        response.raise_for_status()

        html = response.text

        # -------- Nameplate --------
        soup = BeautifulSoup(html, "html.parser")

        info = {}
        for dt, dd in zip(soup.find_all("dt"), soup.find_all("dd")):
            info[dt.get_text(strip=True)] = dd.get_text(strip=True)

        # -------- Hierarchy --------
        hierarchy = {}

        match = re.search(
            r'hierarchy:(\{.*?\})\s*},uses:',
            html,
            re.DOTALL
        )

        if match:
            text = match.group(1)

            # Convert JavaScript object into valid JSON
            text = re.sub(r'(\w+):', r'"\1":', text)

            hierarchy = json.loads(text)

        geo = self.client.get(f"/portal/meters/{meter_id}/geo").json()

        energy = self.client.get(f"/portal/meters/{meter_id}/energy").json()

        return {
            "meter_id": info.get("Meter ID"),
            "serial_no": info.get("Serial No"),
            "make": info.get("Make"),
            "phase_type": info.get("Phase Type"),
            "installation_status": info.get("Installation Status"),
            "installation_type": info.get("Installation Type"),
            "zone": hierarchy.get("Zone"),
            "circle": hierarchy.get("Circle"),
            "division": hierarchy.get("Division"),
            "subdivision": hierarchy.get("Subdivision"),
            "substation": hierarchy.get("Sub Station"),
            "feeder": hierarchy.get("Feeder"),
            "distribution_transformer": hierarchy.get("DT"),
            "location": geo.get("data"),
            "energy": energy.get("data"),
        }