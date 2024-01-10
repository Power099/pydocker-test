import sqlalchemy as sa
import sqlalchemy.orm as so

class Base(so.DeclarativeBase):
    id: so.Mapped[str] = so.mapped_column(primary_key=True)