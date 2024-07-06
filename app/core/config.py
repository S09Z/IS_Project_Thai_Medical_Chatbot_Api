from pydantic import BaseSettings

class Settings(BaseSettings):
    MODEL_NAME: str = "./medical-diagnosis-model"
    PORT: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()
