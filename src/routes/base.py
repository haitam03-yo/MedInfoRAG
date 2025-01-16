from fastapi import FastAPI, APIRouter, Depends
from helpers.config import get_settings, Settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=['api_v1']
)

@base_router.get('/')
async def read_root(app_settings: Settings = Depends(get_settings)):  
    app_settings_dict = app_settings.model_dump()
    app_name = app_settings_dict['APP_NAME']  # Use dictionary key correctly
    app_version = app_settings_dict['APP_VERSION']  # Use dictionary key correctly
    return {"app name": app_name,
            "app version": app_version
            }
    

