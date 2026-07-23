from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from app.client import UrjaPortalClient

app = FastAPI(
    title="Flock Energy API",
    version="1.0.0"
)

portal = UrjaPortalClient()


@app.get("/")
def home():
    return {
        "message": "Flock Energy API"
    }


@app.get("/login")
def login():
    if not portal.login():
        raise HTTPException(
            status_code=401,
            detail="Login failed"
        )

    return {
        "message": "Login successful"
    }


@app.get("/meters")
def meters():
    if not portal.login():
        raise HTTPException(
            status_code=401,
            detail="Login failed"
        )

    data = portal.get_meters()
    return JSONResponse(content=data)


@app.get("/api/v1/meters/{meter_id}")
def meter_details(meter_id: str):
    if not portal.login():
        raise HTTPException(
            status_code=401,
            detail="Login failed"
        )

    data = portal.get_meter_details(meter_id)
    return JSONResponse(content=data)