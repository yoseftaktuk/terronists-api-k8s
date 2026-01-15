from pydantic import BaseModel, Field

class Terrorist(BaseModel):
    name: str
    location: str
    danger_rate: int = Field(...,le=10, gt=0)