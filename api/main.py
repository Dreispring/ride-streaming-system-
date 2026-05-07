from fastapi import FastAPI
from api.routes.trips import router as trips_router

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(trips_router, prefix="/trips")
