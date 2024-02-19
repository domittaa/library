from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

Base = declarative_base()


class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column()
    year: Mapped[int] = mapped_column()
    is_loaned: Mapped[bool] = mapped_column()
    