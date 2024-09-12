import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.const import app_params, uvicorn_params, static_path
from app.core.config import cors_params
from app.routers import main

app = FastAPI(**app_params)

app.mount("/static", StaticFiles(directory=static_path), "static")

app.include_router(main.router)

app.add_middleware(CORSMiddleware, **cors_params)

if __name__ == "__main__":
    uvicorn.run(app, **uvicorn_params)
