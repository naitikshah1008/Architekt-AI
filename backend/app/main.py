from fastapi import FastAPI
from app.api.routes.design import router as design_router

app = FastAPI(title="Architekt AI")

app.include_router(design_router, prefix="/design", tags=["Design"])

@app.get("/")
def root():
    return {"message": "Architekt AI backend is running"}