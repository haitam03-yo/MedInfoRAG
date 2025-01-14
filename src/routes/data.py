from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
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
    is_valid, result_signal = dataController.validate_uploaded_file(file = file)
    if not is_valid:
        return JSONResponse(
                status_code=status.HTTP_INTERNAL_SERVER_ERROR, 
                content={
                    "signal":result_signal
                }
            )
    
    return JSONResponse(
        status_code=status.HTTP_OK,
        content={
            "signal":result_signal,
        }
    )
    