from controller.mission_controller import mission_bluprint
from flask import Flask
from repository.seed_repository import seed

app = Flask(__name__)

if __name__ == '__main__':
    seed()
    app.register_blueprint(mission_bluprint, url_prefix="/api/mission")
    app.run(debug=True)
