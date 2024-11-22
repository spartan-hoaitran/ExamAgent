from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from utils import *
from .v1 import api_key_router,service_router,ai_router
settings=Settings()
port = settings.SERVER_PORT
description=settings.PROJECT_DESCRIPTION
app = FastAPI(
    docs_url=settings.API_STR + '/docs',
    redoc_url=settings.API_STR + '/redoc',
    openapi_url=settings.API_STR + '/openapi.json',
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)
 

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
@app.get(f"{settings.API_STR}")
async def health_method():
    return JSONResponse(content="Server's still alive")
app.include_router(api_key_router, prefix=settings.API_STR, tags=["Api Key API"])
app.include_router(service_router, prefix=settings.API_STR, tags=["System Service API"])
app.include_router(ai_router, prefix=settings.API_STR, tags=["AI API"])