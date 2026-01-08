from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models import ServiceRequest
from app.email_service import send_email

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later restrict for production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/request-service")
def request_service(data: ServiceRequest):
    try:
        send_email(data.name, data.phone)
        return {"message": "Request sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
