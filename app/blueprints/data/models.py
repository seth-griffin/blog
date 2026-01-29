from datetime import date
from typing import Optional
from sqlalchemy import String, Text, Date, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "posts"

    # id INTEGER NOT NULL AUTO_INCREMENT
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # title VARCHAR(64) NOT NULL
    title: Mapped[str] = mapped_column(String(64), nullable=False)

    # posted_on DATE (Allows NULL by default in SQL, so we use Optional)
    posted_on: Mapped[Optional[date]] = mapped_column(Date)

    # categories VARCHAR(128) NOT NULL
    categories: Mapped[Optional[str]] = mapped_column(String(128), nullable=False)

    # content TEXT
    content: Mapped[Optional[str]] = mapped_column(Text)

    # url_path varchar(64) DEFAULT NULL
    url_path: Mapped[Optional[str]] = mapped_column(String(64), server_default=None)

    # Table arguments for MySQL engine and charset
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8mb3",
        "mysql_collate": "utf8mb3_general_ci",
    }
