from typing import Optional
from app.schemas.base import BaseSchema


class ManualSchema(BaseSchema):
    """
    Схема для представления инструкции.

    Attributes:
        id: Уникальный идентификатор инструкции.
        title: Название инструкции.
        file_url: URL для доступа к файлу инструкции.
        cover_image_url: URL изображения обложки инструкции.
        category_id: ID категории, к которой относится инструкция.
        group_id: ID группы, к которой относится инструкция.
    """
    id: Optional[int] = None
    title: str
    file_url: str
    cover_image_url: str
    category_id: int
    group_id: int

    class Config:
        from_attributes = True

class CategorySchema(BaseSchema):
    """
    Схема для представления категории инструкций.

    Attributes:
        id: Уникальный идентификатор категории.
        name: Название категории.
        logo_url: URL логотипа категории.
    """
    id: Optional[int] = None
    name: str
    logo_url: str

    class Config:
        from_attributes = True

class GroupSchema(BaseSchema):
    """
    Схема для представления группы инструкций.

    Attributes:
        id: Уникальный идентификатор группы.
        name: Название группы.
        category_id: ID категории, к которой относится группа.
    """
    id: Optional[int] = None
    name: str
    category_id: int

    class Config:
        from_attributes = True