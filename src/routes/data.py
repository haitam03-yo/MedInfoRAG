from fastapi import FastAPI, APIRouter, Depends, UploadFile
from helpers.config import get_settings, Settings
from controllers import DataController

data_router = APIRouter(
                prefix = "api/v1/data",
                tags=["api_v1"]
            )

@data_router.post('/upload/{project_id}')
def upload_file(project_id: str, file: UploadFile,
                app_settings: Settings = Depends(get_settings)):
    
    dataController = DataController()
    is_valid = dataController.validate_uploaded_file(file = file)
    return is_valid