import factory
from sqlmodel import Session

from .database import engine
from .models import GenderEnum, User


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = Session(engine)
        sqlalchemy_session_persistence = "commit"

    name = factory.Faker("name")
    email = factory.Faker("email")
    active = factory.Faker("pybool")
    gender = factory.Faker("enum", enum_cls=GenderEnum)
    timezone = factory.Faker("pyint", min_value=-12, max_value=14)
    birthday = factory.Faker("date_time_between", start_date="-40y", end_date="-18y")
    location = (
        f'{factory.Faker('city')}, {factory.Faker('state')}'
        if factory.Faker("pybool")
        else None
    )
    had_feedback_email = factory.Faker("pybool")
    sync_name_bio = factory.Faker("pybool")
    bio = factory.Faker("sentence")
