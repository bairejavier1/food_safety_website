from pydantic import BaseModel, Field

class ServiceRequest(BaseModel):
    name: str = Field(..., min_length=2)
    phone: str = Field(..., min_length=10)
