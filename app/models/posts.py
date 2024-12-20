from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Text

from app.models.base import SQLModel
if TYPE_CHECKING:
    from app.models.auth import UserModel  # Импортируем только для проверки типов

class PostModel(SQLModel):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    content: Mapped[str] = mapped_column("content", Text())
    created_at: Mapped[datetime] = mapped_column("created_at", default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column("updated_at", default=datetime.now, onupdate=datetime.now)
    title: Mapped[str] = mapped_column("title", String(100))
    description: Mapped[str] = mapped_column("description", Text())

    author: Mapped["UserModel"] = relationship(back_populates="posts")
    def __repr__(self) -> str:
        return f"Post(id={self.id!r}, title={self.title!r}, description={self.description!r})"
