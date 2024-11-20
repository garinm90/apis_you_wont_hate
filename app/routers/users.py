from fastapi import APIRouter, Depends
from sqlmodel import SQLModel, Session, select

from app.database import get_session
from app.models import GenderEnum, User

router = APIRouter()


class UserPublic(SQLModel):
    name: str
    gender: GenderEnum



@router.get("/users/", response_model=list[UserPublic])
async def read_users(session: Session=Depends(get_session)):
    hereos = session.exec(select(User)).all()
    return hereos

