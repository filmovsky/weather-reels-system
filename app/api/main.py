from fastapi import FastAPI

from app.api.routes.jobs import router as jobs_router
from app.api.routes.regions import router as regions_router
from app.api.routes.voices import router as voices_router
from app.api.routes.layouts import router as layouts_router
from app.api.routes.health import router as health_router

app = FastAPI(title="Weather Reels System")

app.include_router(jobs_router)
app.include_router(regions_router)
app.include_router(voices_router)
app.include_router(layouts_router)
app.include_router(health_router)


@app.get("/")
def root():
    return {"status": "weather reels system running"}