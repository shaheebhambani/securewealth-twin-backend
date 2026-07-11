from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI
from routers import accounts
from database import Base, engine
from routers import transactions
from routers.auth import router as auth_router
from routers import dashboard
from routers import ai
from routers import fraud
from routers import goals
from routers import prediction

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SecureWealth Twin API",
    version="1.0.0"
)

app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to SecureWealth Twin API",
        "status": "Running",
        "version": "1.0"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }
app.include_router(accounts.router)

app.include_router(transactions.router)

app.include_router(dashboard.router)

app.include_router(ai.router)

app.include_router(fraud.router)

app.include_router(goals.router)

app.include_router(prediction.router)

def custom_openapi():

    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        routes=app.routes,
        description="SecureWealth Twin Banking API"
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    for path in openapi_schema["paths"].values():
        for operation in path.values():
            operation["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi