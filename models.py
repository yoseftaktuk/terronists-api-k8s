from pydantic import BaseModel, Field

class Terrorist(BaseModel):
     name: str = Field(default=None)
     location: str = Field(default=None) 
     danger_rate: int = Field(default=None, le=10, gt=0)