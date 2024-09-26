from repository.mission_repository import get_all_missions, get_mission_by_id


def test_get_all_missions():
    res = get_all_missions()
    assert res
