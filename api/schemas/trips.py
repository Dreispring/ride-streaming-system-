from pydantic import BaseModel

class TripRequest(BaseModel):
    user_id: str
    distance_km: float
    destination: str
