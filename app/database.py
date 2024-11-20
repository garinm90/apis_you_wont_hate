from enum import Enum
from sqlmodel import Field, Session, SQLModel, create_engine, select

class GenderEnum(str, Enum):
    MALE = "male"
    FEMALE = "female"


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str
    active: bool = Field(default=False)
    gender: GenderEnum
    age: int | None = Field(default=None, index=True)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)