from fastapi import APIRouter
from api.services.trips_service import create_trip, get_trips
from api.schemas.trips import TripRequest

router = APIRouter()

@router.post("/")
def create_trip_api(trip: TripRequest):
    return create_trip(trip.model_dump())

@router.get("/")
def fetch_trips():
    return get_trips()
