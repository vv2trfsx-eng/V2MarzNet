from fastapi import FastAPI
from api.routes import router


app.include_router(
    router,
    prefix="/api"
)
app = FastAPI(
    title="V2MarzNet API",
    description="Professional VPN Management Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "V2MarzNet",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "health": "ok"
    }
