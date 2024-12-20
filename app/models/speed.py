"""
Модуль, содержащий модели данных для настройки скоростей моталки.

Этот модуль определяет следующие модели SQLAlchemy:
- ReelModel: представляет моталку
- RollModel: представляет формирующий ролик моталки
- SpeedModel: представляет параметры скоростей формирующего ролика моталки

Каждая модель наследуется от базового класса SQLModel и определяет 
соответствующие поля и отношения между таблицами базы данных.

Модели используют типизированные аннотации Mapped для определения полей,
что обеспечивает улучшенную поддержку статической типизации.

Этот модуль предназначен для использования в сочетании с SQLAlchemy ORM
для выполнения операций с базой данных, связанных с инструкциями по эксплуатации.
"""
from datetime import datetime
from typing import List
import pytz

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from app.models.base import SQLModel

moscow_tz = pytz.timezone('Europe/Moscow')

class ReelModel(SQLModel):
    """
    Модель для представления моталки.

    Attributes:
        id (int): Уникальный идентификатор моталки.
        name (str): Название моталки.
        rolls (relationship): Формирующие ролики, относящиеся к этой категории.

    Methods:
        __init__(id: int, name: str) -> None: Инициализирует объект ReelModel.
        __repr__() -> str: Возвращает строковое представление объекта ReelModel.
        __str__() -> str: Возвращает строковое представление объекта ReelModel.

    Raises:
        ValueError: Если id или name не являются допустимыми значениями.

    Examples:
        >>> reel = ReelModel(id=1, name="Моталка 1")
        >>> print(reel.name)
        Моталка 1
    """
    __tablename__ = "reels"

    id: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    name: Mapped[str] = mapped_column("reel_name", String(100))

    rolls: Mapped[List["RollModel"]] = relationship("RollModel", back_populates="reel")

class RollModel(SQLModel):
    """
    Модель для представления формирующих роликов моталки.

    Attributes:
        id (int): Уникальный идентификатор формирующего ролика.
        name (str): Название формирующего ролика.
        reel_id (int): ID моталки, к которой относится формирующий ролик.
        reel (relationship): Моталка, к которой относится формирующий ролик.
        speeds (relationship): Параметры скорости, относящиеся к этому формирующему ролику.

    Methods:
        __init__(id: int, name: str, reel_id: int) -> None: Инициализирует объект RollModel.
        __repr__() -> str: Возвращает строковое представление объекта RollModel.
        __str__() -> str: Возвращает строковое представление объекта RollModel.

    Raises:
        ValueError: Если id, name или reel_id не являются допустимыми значениями.

    Examples:
        >>> roll = RollModel(id=1, name="Формирующий ролик 1", reel_id=1)
        >>> print(roll.name)
        Формирующий ролик 1
    """
    __tablename__ = "rolls"

    id: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    name: Mapped[str] = mapped_column("roll_name", String(100))
    reel_id: Mapped["int"] = mapped_column(ForeignKey(ReelModel.id, ondelete="CASCADE"))
        
    reel: Mapped["ReelModel"] = relationship("ReelModel", back_populates="rolls")
    speeds: Mapped[List["SpeedModel"]] = relationship("SpeedModel", back_populates="rolls")

class SpeedModel(SQLModel):
    """
    Модель для представления параметров скорости формирующего ролика моталки.

    Attributes:
        id (int): Уникальный идентификатор параметра скорости.
        task (float): Задача, для которой определяется параметр скорости.
        tspd (int): Текущая скорость.
        fspd (bool): Флаг, указывающий на то, что скорость является фиксированной.
        bmav (int): Базовая скорость.
        bemf (float): Базовый электромагнитный момент.
        amav (int): Активная скорость.
        aemf (float): Активный электромагнитный момент.
        memf (float): Максимальный электромагнитный момент.
        corr (bool): Флаг, указывающий на то, что скорость является корректированной.
        created_at (datetime): Дата и время создания параметра скорости.
        updated_at (datetime): Дата и время последнего обновления параметра скорости.
        roll (relationship): Формирующий ролик, к которому относится этот параметр скорости.
    """
    __tablename__ = "speeds"

    id: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    task: Mapped[float] = mapped_column("task", nullable=False)
    tspd: Mapped[int] = mapped_column("tspd", nullable=False)
    fspd: Mapped[bool] = mapped_column("fspd", nullable=False)
    bmav: Mapped[int] = mapped_column("bmav", nullable=False)
    bemf: Mapped[float] = mapped_column("bemf", nullable=False)
    amav: Mapped[int] = mapped_column("amav", nullable=False)
    aemf: Mapped[float] = mapped_column("aemf", nullable=False)
    memf: Mapped[float] = mapped_column("memf", nullable=False)
    corr: Mapped[bool] = mapped_column("corr", nullable=False)
    created_at: Mapped[datetime] = mapped_column("created_at", default=lambda: datetime.now(moscow_tz))
    updated_at: Mapped[datetime] = mapped_column("updated_at", default=lambda: datetime.now(moscow_tz), onupdate=lambda: datetime.now(moscow_tz))
    roll: Mapped["RollModel"] = relationship("RollModel", back_populates="speeds")
    roll_id: Mapped[int] = mapped_column(ForeignKey(RollModel.id, ondelete="CASCADE"))
