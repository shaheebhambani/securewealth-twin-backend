from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

app = FastAPI(
    title="SecureWealth Twin API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "SecureWealth Twin Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }