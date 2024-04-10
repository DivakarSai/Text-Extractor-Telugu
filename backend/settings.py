from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Your FastAPI Application"
    admin_email: str
    database_url: str
    secret_key: str
    debug: bool = False

    class Config:
        env_file = ".env"  # Load environment variables from .env file

settings = Settings()
