from typing import List

from returns.maybe import Maybe, Nothing, Some
from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError

from config.base import session_factory
from model import Mission


def get_all_missions() -> List[Mission]:
    with session_factory() as session:
        return session.query(Mission).all()

def get_mission_by_id()