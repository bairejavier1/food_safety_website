from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .models import ServiceRequest
from .email_service import send_service_request_email

app = FastAPI(title="Food Safety Service API")

# Allow all origins during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/request-service")
def create_service_request(request: ServiceRequest):
    print("📥 Received service request:", request)

    try:
        send_service_request_email(request)
    except Exception as e:
        print("❌ Backend error:", e)
        raise HTTPException(status_code=500, detail=f"Email failed: {e}")

    return {"message": "Service request submitted successfully"}
