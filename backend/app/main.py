from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .models import ServiceRequest
from .email_service import send_service_request_email

app = FastAPI(title="Food Safety Service API")

# Adjust origins if you deploy with a different URL
origins = [
    "http://localhost:5500",  # example if serving static files with Live Server
    "http://localhost:8000",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8000",
    # Add your production domain here when you have one
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/request-service")
def create_service_request(request: ServiceRequest):
    try:
        send_service_request_email(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {e}")

    return {"message": "Service request submitted successfully"}
