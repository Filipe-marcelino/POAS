from sqlmodel import SQLModel,Field
from datetime import datetime
from pydantic import EmailStr

class Usuario(SQLModel, table=True):
    id:int = Field(default=None, primary_key=True)
    nome:str = Field(default=None, nullable=False)
    email: EmailStr = Field(default=None, nullable=False, unique=True)
    senha:hash = Field(default=None, nullable=False)
    criadoEm:datetime = Field(default_factory=datetime.utcnow)

class Papeis(SQLModel, table=True):
    id:int = Field(default=None, primary_key=True)
    nome:str = Field(default=None, nullable=False)

class UsuarioPapeis(SQLModel, table=True):
    usuario_id:int = Field(default=None, foreign_key='usuario.id')
    papeis_id:int = Field(default=None, foreign_key='papeis.id')

class Produtos(SQLModel, table=True):
    id:int  = Field(default=None, primary_key=True)
    nome:str = Field(default=None, nullable=False)
    descricao:str = Field(default=None, nullable=False)
    preco:float = Field(default=None, nullable=False)
    criadoEm:datetime = Field(default_factory=datetime.utcnow)

class Categorias(SQLModel, table=True):
    id:int  = Field(default = None, primary_key = True)
    nome:str = Field(default=None, nullable=False)

class ProdutoCategorias(SQLModel, table=True):
    produtos_id:int = Field(default=None, foreign_key='produtos.id')
    categorias_id:int = Field(default=None, foreign_key='categorias.id')

class Pedidos(SQLModel, table=True):
    id:int  = Field(default=None, primary_key=True)
    total:float = Field(default=None, nullable=False)
    status:str = Field(default=None, nullable=False)
    criadoEm:datetime = Field(default_factory=datetime.utcnow)
    usuario_id:int = Field(default=None, foreign_key='usuario.id')

class ItensPedidos(SQLModel, table=True):
    id:int  = Field(default=None, primary_key=True)
    quantidade:int = Field(index=False)
    preco:float = Field(index=False)
    pedidos_id:int = Field(foreign_key='pedidos.id')
    produtos_id:int = Field(foreign_key='produtos.id')

class Pagamentos(SQLModel, table=True):
    id:int  = Field(default=None, primary_key=True)
    valor:float = Field(default=None, nullable=False)
    metodo:str = Field(default=None, nullable=False)
    status:str = Field(default=None, nullable=False)
    criadoEm:datetime = Field(default_factory=datetime.utcnow)
    pedidos_id:int = Field(foreign_key='pedidos.id')

class Endereco(SQLModel, table=True):
    id:int  = Field(default=None, primary_key=True)
    usuario_id:int = Field(primary_key=True)
    rua:str = Field(default=None, nullable=False)
    cidade:str = Field(default=None, nullable=False)
    estado:str = Field(default=None, nullable=False)
    cep:str = Field(default=None, nullable=False)
    usuario_id:int = Field(foreign_key='usuario.id')

class AValiacoes(SQLModel, table=True):
    id:int  = Field(default=None, primary_key=True)
    usuario_id:int = Field(primary_key=True)
    produtos_id:int = Field(primary_key=True)
    nota:int = Field(default=None, nullable=False)
    comentario:str = Field(default=None, nullable=False)
    criadoEm:datetime = Field(default_factory=datetime.utcnow)
    usuario_id:int = Field(foreign_key='usuario.id')
    produtos_id:int = Field(foreign_key='produtos.id')

class Estoque(SQLModel, table=True):
    id:int  = Field(default=None, primary_key=True)
    quantidade:int = Field(default=None, nullable=False)
    atualizadoEm:datetime = Field(default_factory=datetime.utcnow)
    produtos_id: int = Field(foreign_key='produtos.id')
    