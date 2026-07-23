# Flock Energy API Wrapper

A FastAPI-based REST API wrapper for the legacy **Urja Meter Ops** portal. This project provides a clean and documented API over the existing web application by automating access to meter information, hierarchy, location, and energy consumption data.

---

# Features

- Session-based authentication
- Retrieve available smart meters
- Fetch detailed meter information
- Retrieve network hierarchy
- Fetch meter geo-location
- Fetch energy consumption history
- Clean REST API built with FastAPI
- Interactive Swagger UI
- OpenAPI 3 Specification

---

# Tech Stack

- Python 3.10+
- FastAPI
- HTTPX
- BeautifulSoup4
- Uvicorn

---

# Project Structure

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
├── .env.example
├── PROTOCOL.md
├── openapi.json
├── README.md
├── requirements.txt
├── Dockerfile
└── .gitignore
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/Abhishek-NIT-btech/FLOCK-ENERGY-API.git

cd FLOCK-ENERGY-API
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
BASE_URL=https://urja-ops.flockenergy.tech
SESSION_COOKIE=your_session_cookie_here
```

Run the application

```bash
uvicorn app.main:app --reload --port 8005
```

---

# API Documentation

Swagger UI

```
http://127.0.0.1:8005/docs
```

OpenAPI Specification

```
/openapi.json
```

---

# Available Endpoints

## Home

```
GET /
```

## Login

```
GET /login
```

## List Meters

```
GET /meters
```

## Meter Details

```
GET /api/v1/meters/{meter_id}
```

Example

```
GET /api/v1/meters/J100000
```

---

# Sample Response

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

---

# Design Decisions & Trade-offs

- FastAPI was chosen because it automatically generates OpenAPI documentation and provides excellent developer experience.
- HTTPX was used to maintain persistent HTTP sessions while communicating with the legacy portal.
- BeautifulSoup4 was used to parse HTML responses returned by the portal.
- Multiple portal responses are combined into a single clean JSON response for easier consumption.
- The application follows a modular architecture by separating configuration, client logic, parsing, models, and API routes.

---

# Assumptions

- The Urja portal uses session-based authentication.
- The HTML structure of the portal remains reasonably consistent.
- The discovered endpoints continue to expose meter, hierarchy, geo-location, and energy data.
- Users accessing this API have valid credentials for the portal.

---

# What I Intentionally Skipped

- Response caching
- Retry mechanisms
- Bulk synchronization of all meters
- Advanced filtering and searching
- Automated unit and integration tests

These features were intentionally left out to focus on delivering the core API functionality within the assignment timeline.

---

# Future Improvements

- Implement automatic authentication using username and password.
- Automatic session renewal when authentication expires.
- Improve HTML parser robustness.
- Add response caching.
- Add unit and integration tests.
- Improve logging and monitoring.
- Support bulk data export.
- Improve error handling and validation.

---

# Reflection

## What assumptions did you make?

I assumed the legacy portal uses session-based authentication and that the HTML layout would remain reasonably consistent for extracting the required information.

## Which part was the most difficult?

The most challenging part was understanding how the legacy portal communicated internally and identifying the endpoints that contained the required meter information. Parsing HTML into structured JSON also required careful inspection.

## If you had another day, what would you improve?

I would implement automatic login using credentials instead of relying on an existing authenticated session, improve parser resilience, add automated tests, introduce caching, and provide more comprehensive error handling.

## What mistake did you make?

Initially I relied on an authenticated browser session during development. A production-ready implementation should automatically authenticate and renew expired sessions.

## If you were reviewing your own submission, what would you criticise?

I would improve authentication handling, increase parser robustness against changes in HTML structure, and add automated tests to improve long-term maintainability.

---

# Additional Documentation

This repository also contains:

- **PROTOCOL.md** — Authentication workflow, endpoint discovery, and portal behaviour.
- **openapi.json** — OpenAPI 3 specification generated from the FastAPI application.

---

# Author

**Karri Veera Venkata Abhishek Reddy**

B.Tech, Electronics and Communication Engineering

National Institute of Technology Durgapur