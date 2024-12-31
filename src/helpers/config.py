from pydantic_settings import BaseModel

class Settings(BaseModel):
    APP_NAME:str
    APP_VERSION:str
    OPENAI_API_KEY:str
    
    class config:
        env_file = ".env"
        
def get_settings():
    return Settings()