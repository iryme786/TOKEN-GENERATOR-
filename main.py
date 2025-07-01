import os
from fastapi import FastAPI, Request
import requests
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

BASE_HEADERS = {
    "User-Agent": "Classplus/1.4.58 Android/11",
    "Content-Type": "application/json",
    "x-access-token": "null",
}

@app.post("/send-otp")
async def send_otp(request: Request):
    data = await request.json()
    org_code = data.get("orgCode")
    phone = data.get("phoneNumber")

    response = requests.post(
        "https://prod-api.classplusapp.com/v2/customer/sendAppLink",
        json={"orgCode": org_code, "phoneNumber": phone},
        headers=BASE_HEADERS
    )
    return response.json()

@app.post("/verify-otp")
async def verify_otp(request: Request):
    data = await request.json()
    org_code = data.get("orgCode")
    phone = data.get("phoneNumber")
    otp = data.get("otp")

    response = requests.post(
        "https://prod-api.classplusapp.com/v2/customer/verifyOtp",
        json={"orgCode": org_code, "phoneNumber": phone, "otp": otp},
        headers=BASE_HEADERS
    )
    return response.json()
