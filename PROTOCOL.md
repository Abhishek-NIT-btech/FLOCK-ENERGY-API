# PROTOCOL.md

# Authentication

- Portal URL: https://urja-ops.flockenergy.tech
- Authentication is session-based.
- Login requires username and password.
- After authentication, the server issues a session cookie that is reused for subsequent requests.

# Internal Endpoints Discovered

| Method | Endpoint | Purpose |
|---------|----------|---------|
| GET | /login | Authentication |
| GET | /portal/meters/search | List meters |
| GET | /meters/{meter_id} | Meter details |
| GET | /portal/meters/{meter_id}/geo | Meter location |
| GET | /portal/meters/{meter_id}/energy | Energy consumption |

# Data Retrieved

- Meter ID
- Serial Number
- Meter Make
- Phase Type
- Installation Status
- Installation Type
- Zone
- Circle
- Division
- Subdivision
- Substation
- Feeder
- Distribution Transformer
- Geo Location
- Energy Consumption

# Observations

- The portal primarily returns HTML pages.
- BeautifulSoup was used to parse meter information.
- Additional information such as geo location and energy data is available through JSON endpoints.
- Session persistence is required for accessing protected resources.