from sqlmodel import SQLModel,Field
from datetime import datetime

class Usuario(SQLModel, table=True):
    id:int |None = Field(default=None, primary_key=True)
    nome:str = Field(index=False)
    email:str = Field(unique=True,index=True)
    senha:hash = Field(index=False)
    criadoEm:datetime = Field(default_factory=datetime.utcnow)

class Papeis(SQLModel, table=True):
    id:int |None = Field(default=None, primary_key=True)
    nome:str = Field(index=False)

class UsuarioPapeis(SQLModel, table=True):
    usuario_id:int = Field()
    usuario_id:int = Field(foreign_key='usuario.id')
    papeis_id:int = Field(foreign_key='papeis.id')