from pydantic import BaseSettings
from pydantic.main import BaseModel

class MiddleWareBase(BaseModel):
    host: str
    port: int
    password: str


class DbStruct(MiddleWareBase):
    user: str
    pool_size: int = 30
    max_overflow: int = 100

class Settings(BaseSettings):
    PROJECT_NAME: str = "pydocker"

    DB_MYSQL: DbStruct

    DB_NAME="pydocker"

    class Config:
        case_sensitive = True
        env_file = ".env"
        
settings = Settings()  # type: ignore