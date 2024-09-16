"""
Модуль, содержащий модели данных для работы с инструкциями по эксплуатации.

Этот модуль определяет следующие модели SQLAlchemy:
- ManualModel: представляет инструкцию по эксплуатации
- CategoryModel: представляет категорию инструкций
- GroupModel: представляет группу инструкций

Каждая модель наследуется от базового класса SQLModel и определяет 
соответствующие поля и отношения между таблицами базы данных.

Модели используют типизированные аннотации Mapped для определения полей,
что обеспечивает улучшенную поддержку статической типизации.

Этот модуль предназначен для использования в сочетании с SQLAlchemy ORM
для выполнения операций с базой данных, связанных с инструкциями по эксплуатации.
"""
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import MetaData, String, ForeignKey#, event
from app.models.base import SQLModel, CoverURLType
from sqlalchemy import func

class ManualModel(SQLModel):
    """
    Модель для представления инструкции по эксплуатации.

    Attributes:
        id (int): Уникальный идентификатор инструкции.
        title (str): Название инструкции.
        file_url (str): URL для скачивания/открытия файла инструкции.
        cover_image_url (str): URL изображения обложки инструкции.
        category_id (int): ID категории, к которой относится инструкция.
        group_id (int): ID группы, к которой относится инструкция.
    """
    __tablename__ = "manuals"

    metadata = MetaData()

    id: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    title: Mapped[str] = mapped_column("title", String(200))
    file_url: Mapped[str] = mapped_column("file_url", String)
    cover_image_url: Mapped[str] = mapped_column("cover_image_url", String, default=func.CoverURLType(file_url))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE", use_alter=True))
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id", ondelete="CASCADE", use_alter=True))

    __table_args__ = {'schema': 'GroupModel'} if 'GroupModel' else {}

    # @event.listens_for(ManualModel, 'before_insert')
    # @event.listens_for(ManualModel, 'before_update')
    # def generate_column(mapper, connection, target):
    #     target.cover_image_url = CoverURLType(target.source_column)

class CategoryModel(SQLModel):
    """
    Модель для представления категории инструкций.

    Attributes:
        id (int): Уникальный идентификатор категории.
        name (str): Название категории.
        logo_url (str): URL логотипа категории.
    """
    __tablename__ = "categories"

    metadata = MetaData()

    id: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    name: Mapped[str] = mapped_column("category_name", String(100))
    logo_url: Mapped[str] = mapped_column("logo_url", default="/media/manuals/default-logo.png")


class GroupModel(SQLModel):
    """
    Модель для представления группы инструкций.

    Attributes:
        id (int): Уникальный идентификатор группы.
        name (str): Название группы.
        category_id (int): ID категории, к которой относится группа.
    """
    __tablename__ = "groups"

    metadata = MetaData()

    id: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    name: Mapped[str] = mapped_column("group_name", String(100))
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", 
                        ondelete="CASCADE",
                        use_alter=True)
    )
    __table_args__ = {'schema': 'CategoryModel'} if 'CategoryModel' else {}