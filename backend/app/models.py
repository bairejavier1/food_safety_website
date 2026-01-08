from pydantic import BaseModel, Field

class ServiceRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    phone: str = Field(..., min_length=7, max_length=20)
    message: str | None = Field(default=None, max_length=500)
