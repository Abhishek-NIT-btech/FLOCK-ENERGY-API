# Flock Energy API Wrapper

A FastAPI-based API wrapper for the Urja Ops Portal.

## Features

- Authenticate using session cookie
- Retrieve available meters
- Fetch meter details
- Fetch hierarchy information
- Fetch meter location (Latitude & Longitude)
- Fetch energy consumption history
- Exposes a unified REST API

## Tech Stack

- Python 3
- FastAPI
- HTTPX
- BeautifulSoup4
- Uvicorn

## Project Structure

```
FLOCK-ENERGY-API/
│
├── app/
│   ├── routes/
│   ├── client.py
│   ├── config.py
│   ├── main.py
│   ├── models.py
│   └── parser.py
│
├── .env
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add:

```env
BASE_URL=https://urja-ops.flockenergy.tech
SESSION_COOKIE=your_session_cookie_here
```

4. Run the application:

```bash
uvicorn app.main:app --reload --port 8005
```

## API Documentation

Swagger UI:

```
http://127.0.0.1:8005/docs
```

## Available Endpoints

### Login

```
GET /login
```

### List Meters

```
GET /meters
```

### Meter Details

```
GET /api/v1/meters/{meter_id}
```

Example:

```
GET /api/v1/meters/J100000
```

## Sample Response

```json
{
  "meter_id": "J100000",
  "serial_no": "SE33962",
  "make": "HPL",
  "phase_type": "single",
  "installation_status": "Decommissioned",
  "installation_type": "Whole Current",
  "zone": "Jaipur Zone 1 (Z-01)",
  "circle": "Circle 1 (C-01)",
  "division": "Division 1 (D-01)",
  "subdivision": "Subdivision 1 (SD-01)",
  "substation": "Substation 1 (SS-01)",
  "feeder": "Feeder 1 (F-001)",
  "distribution_transformer": "Malviya Nagar DT 1 (DT-001)",
  "location": {
    "latitude": "26.938961002479868",
    "longitude": "75.83095696146852"
  },
  "energy": [
    {
      "timestamp": "23/06/2026 23:30",
      "kwh": "48438.74",
      "kvah": "52313.84",
      "voltR": "226"
    }
  ]
}
```