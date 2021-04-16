from flask import request
from resources.utils import genExpDateInMilSecs
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_restful import Resource
import datetime
from app import db
from .schemas import usuarios_schema, usuario_schema, paciente_schema, pacientes_schema
from .models import Paciente, Usuario
from resources.errors import CredentialsInvalidError, MissingAuthorizationTokenError, UnauthorizedError, InternalServerError
from flask_jwt_extended.exceptions import NoAuthorizationError


class UsuariosResource(Resource):
    @jwt_required()
    def get(self):
        try:
            usuario = Usuario.query.get(get_jwt_identity())

            if not usuario.isAdmin():
                return {'erro': "Usuário não é administrador"}, 401

            usuarios = Usuario.query.all()
            return usuarios_schema.dump(usuarios)
        except Exception as e:
            raise InternalServerError


class UsuarioResource(Resource):
    def post(self):
        try:
            body = request.get_json()
            usuario = Usuario(**body)
            usuario.hash_password()
            db.session.add(usuario)
            db.session.commit()
            return usuario_schema.dump(usuario)
        except Exception as e:
            return e


class LoginResource(Resource):
    def post(self):
        try:
            body = request.get_json()
            usuario: Usuario = Usuario.query.filter_by(
                email=body.get('email')).first()
            authorized = usuario.check_password(body.get('senha'))

            if not authorized:
                return {'erro': 'E-mail ou senha inválidos'}, 401
                # raise CredentialsInvalidError

            expires = datetime.timedelta(days=1)
            expirationDate = genExpDateInMilSecs(expires)
            access_token = create_access_token(identity=str(
                usuario.id__usuario), expires_delta=expires,)
            return {'token': access_token, 'nome': usuario.nome, 'email': usuario.email, 'expires': expirationDate}, 200
        except (UnauthorizedError):
            raise UnauthorizedError
        except (CredentialsInvalidError):
            raise CredentialsInvalidError
        except (Exception) as e:
            raise InternalServerError


class PacientesResource(Resource):
    @jwt_required()
    def get(self):
        try:
            pacientes = Paciente.query.all()
            return pacientes_schema.dump(pacientes)
        except Exception as e:
            return e

    @jwt_required()
    def post(self):
        try:
            body = request.get_json()
            paciente = Paciente(**body)
            db.session.add(paciente)
            db.session.commit()
            return paciente_schema.dump(paciente)
        except Exception as e:
            return e


class PacienteResource(Resource):
    @jwt_required()
    def get(self, id):
        try:
            paciente = Paciente.query.get(id)
            return paciente_schema.dump(paciente)
        except Exception as e:
            return e

    @jwt_required()
    def put(self, id):
        try:
            body = request.get_json()
            paciente = Paciente.query.filter_by(id__paciente=id).update(body)
            db.session.commit()
            return {"id": id, "resultado": paciente}
        except NoAuthorizationError as e:
            raise MissingAuthorizationTokenError
        except Exception as e:
            raise InternalServerError
