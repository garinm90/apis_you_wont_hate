from datetime import date
from enum import Enum
from sqlmodel import Field, SQLModel


class GenderEnum(str, Enum):
    MALE = "male"
    FEMALE = "female"


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str
    active: bool = Field(default=False)
    gender: GenderEnum
    timezone: int
    birthday: date
    location: str = Field(nullable=True)
    had_feedback_email: bool
    sync_name_bio: bool
    bio: str
