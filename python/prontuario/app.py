from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_restful import Api

from resources import errors

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')



# api = Api(app, errors=errors)
api = Api(app)
jwt = JWTManager(app)


db = SQLAlchemy(app)
ma = Marshmallow(app)
db.init_app(app)

from resources.routes import initialize_routes
initialize_routes(api)
