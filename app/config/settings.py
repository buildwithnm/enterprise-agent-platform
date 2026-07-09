from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    OLLAMA_HOST: str
    MODEL_NAME: str
    PROVIDER: str

    class Config:
        env_file = ".env"


settings = Settings()
