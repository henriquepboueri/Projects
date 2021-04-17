from flask_restful import Api
from .resources import CovidAnamneseResource, LoginResource, PacienteResource, PacientesResource, UsuariosResource


def initialize_routes(api: Api):
    # url_base = '/api/v1/'

    api.add_resource(UsuariosResource, '/api/v1/usuarios')
    # api.add_resource(UsuarioResource, '/api/usuario')

    api.add_resource(LoginResource, '/api/v1/auth/login')

    # api.add_resource(PacientesResource, '/api/paciente')
    api.add_resource(PacienteResource, '/api/v1/paciente/<id>')
    api.add_resource(PacientesResource, '/api/v1/pacientes')

    api.add_resource(CovidAnamneseResource, '/api/v1/covid')
