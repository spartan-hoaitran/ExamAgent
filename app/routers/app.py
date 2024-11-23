from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from utils import *
from .v1 import exam_router 
# from .v1 import api_key_router,service_router,ai_router
from utils.config import get_settings
settings=get_settings()
port = settings.SERVER_PORT
description=settings.PROJECT_DESCRIPTION
print(settings.API_STR + '/docs')
api= FastAPI(
    docs_url=settings.API_STR + '/docs',
    redoc_url=settings.API_STR + '/redoc',
    openapi_url=settings.API_STR + '/openapi.json',
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)
 

# if settings.BACKEND_CORS_ORIGINS:
#     api.add_middleware(
#         CORSMiddleware,
#         allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )
@api.get(f"{settings.API_STR}")
async def health_method():
    return JSONResponse(content="Server's still alive")
api.include_router(exam_router, prefix=settings.API_STR, tags=["Exam API"])
# api.include_router(service_router, prefix=settings.API_STR, tags=["System Service API"])
# api.include_router(ai_router, prefix=settings.API_STR, tags=["AI API"])