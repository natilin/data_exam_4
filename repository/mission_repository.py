from typing import List

from returns.maybe import Maybe, Nothing, Some


from config.base import session_factory
from model import Mission


def get_all_missions() -> List[Mission]:
    with session_factory() as session:
        return session.query(Mission).all()


def get_mission_by_id(m_id: int) -> Maybe[Mission]:
    with session_factory() as session:
        return Maybe.from_optional(
            session.query(Mission)
            .filter(m_id == Mission.mission_id)
            .first()
        )
