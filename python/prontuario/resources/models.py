from app import db
from flask_bcrypt import generate_password_hash, check_password_hash

from app import db


class TipoUsuario(db.Model):
    __tablename__ = 'tipo_usuario'

    id__tipo_usuario = db.Column(db.BigInteger, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    data_cadastro = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue())


class Usuario(db.Model):
    __tablename__ = 'usuario'

    id__usuario = db.Column(db.BigInteger, primary_key=True)
    id__tp_usuario = db.Column(db.ForeignKey(
        'tipo_usuario.id__tipo_usuario'), nullable=False, index=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    data_cadastro = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue())

    tipo_usuario = db.relationship(
        'TipoUsuario', primaryjoin='Usuario.id__tp_usuario == TipoUsuario.id__tipo_usuario', backref='usuarios')

    def hash_password(self):
        self.senha = generate_password_hash(self.senha).decode('utf8')

    def check_password(self, senha):
        return check_password_hash(self.senha, senha)

    def isAdmin(self):
        return self.tipo_usuario.nome == 'Admin'


class Paciente(db.Model):
    __tablename__ = 'paciente'

    id__paciente = db.Column(db.BigInteger, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50))
    nr_sus = db.Column(db.String(50))
    sexo = db.Column(db.String(1), nullable=False)
    dt_nasc = db.Column(db.Date, nullable=False)
    cor = db.Column(db.String(1))
    nm_mae = db.Column(db.String(100))
    nm_pai = db.Column(db.String(100))
    cep = db.Column(db.String(8))
    logradouro = db.Column(db.String(100))
    bairro = db.Column(db.String(50))
    numero = db.Column(db.String(50))
    cidade = db.Column(db.String(100))
    nr_telefone_1 = db.Column(db.String(11))
    nr_telefone_2 = db.Column(db.String(11))
    profissao = db.Column(db.String(50))
    nmContato = db.Column(db.String(100))
    nr_contato = db.Column(db.String(11))
    obs_contato = db.Column(db.String)
    obs_gerais = db.Column(db.String)
    data_cadastro = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue())
