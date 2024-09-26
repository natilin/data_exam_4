from dictalchemy.utils import asdict
from returns.maybe import Some

from repository.mission_repository import get_mission_by_id, get_all_missions
from flask import Blueprint,  jsonify

mission_bluprint = Blueprint("missions", __name__)


@mission_bluprint.route('/', methods=['GET'])
def get_all():
    res = get_all_missions()
    return jsonify([asdict(m) for m in res]), 200


@mission_bluprint.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    res = get_mission_by_id(id)
    return (jsonify(asdict(res.unwrap())), 200) if isinstance(res, Some) else (jsonify({"error": "Not found"}), 404)