"""
main python file
"""

from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api

from databases.db import db
from resources.category import category_blueprint

app = Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"] = True
# TODO: generate swagger
app.config["API_TITLE"] = "Simple Store REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger"
app.config[
    "OPENAPI_SWAGGER_URL"
] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  # noqa
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:postgrespw@localhost:5432/db_flask_simple_store"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)


api = Api(app)
api.register_blueprint(category_blueprint)

if __name__ == "__main__":
    app.run(port=9000, debug=True)
