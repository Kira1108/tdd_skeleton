import logging
logger = logging.getLogger('uvicorn')

from fastapi import FastAPI
from app.api import ping, summarize
from app.db import init_db

def create_app():
    app = FastAPI()
    app.include_router(ping.router)
    app.include_router(summarize.router)
    return app

app = create_app()

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")
    init_db()


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
    
    
