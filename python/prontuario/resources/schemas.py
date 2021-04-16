from app import ma
from .models import Paciente, TipoUsuario, Usuario


class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    # class UsuarioSchema(ma.Schema):
    class Meta:
        # fields = ('nome', 'email', 'senha')
        model = Usuario


class TipoUsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TipoUsuario


class PacienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Paciente


usuarios_schema = UsuarioSchema(many=True)
usuario_schema = UsuarioSchema()

paciente_schema = PacienteSchema()
pacientes_schema = PacienteSchema(many=True)