import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.dialects.mysql import TINYINT
from utils import generate_id
from .db import Base


class UserInfo(Base):
    __tablename__ = "t_user_info"
    __table_args__ = ({"comment": "user table"},)
    id: so.Mapped[str] = so.mapped_column(
        sa.String(32),
        primary_key=True,
        default=lambda: generate_id("u"),
        comment="业务主键",
    )
    user_name: so.Mapped[str] = so.mapped_column(
        sa.String(200), nullable=False, comment="用户名"
    )
    password: so.Mapped[str] = so.mapped_column(
        sa.String(500), nullable=False, comment="密码"
    )
 