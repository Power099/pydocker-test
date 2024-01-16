from sqlalchemy import create_engine
from configs import settings

db_info = settings.DB_MYSQL
connection_str = f"{db_info.user}:{db_info.password}@{db_info.host}:{db_info.port}"

engine = create_engine(
    f"pymysql://{connection_str}/{settings.DB_NAME}?charset=utf8mb4",
    echo=False,
    pool_size=db_info.pool_size,
    max_overflow=db_info.max_overflow,
    pool_recycle=14400,
    pool_pre_ping=True,
)

session_args = {
    "autocommit": False,
    "autoflush": True,
    "expire_on_commit": False,
}
