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
    usuario_id:int = Field(primary_key=True)
    papeis_id:int = Field(primary_key=True)
    usuario_id:int = Field(foreign_key='usuario.id')
    papeis_id:int = Field(foreign_key='papeis.id')

class Produtos(SQLModel, table=True):
    id:int |None = Field(default=None, primary_key=True)
    nome:str = Field(index=False)
    descricao:str = Field(index=False)
    preco:float = Field(index=False)
    criadoEm:datetime = Field(default_factory=datetime.utcnow)

class Categorias(SQLModel, table=True):
    id:int |None = Field(default = None, primary_key = True)
    nome:str = Field(index=False)

class ProdutoCategorias(SQLModel, table=True):
    produtos_id:int = Field(primary_key=True)
    categorias_id:int = Field(primary_key=True)
    produtos_id:int = Field(foreign_key='produtos.id')
    categorias_id:int = Field(foreign_key='categorias.id')

class Pedidos(SQLModel, table=True):
    id:int |None = Field(default=None, primary_key=True)
    usuario_id:int = Field(primary_key=True)
    total:float = Field(index=False)
    status:str = Field(index=False)
    criadoEm:datetime = Field(default_factory=datetime.utcnow)
    usuario_id:int = Field(foreign_key='usuario.id')

class ItensPedidos(SQLModel, table=True):
    id:int |None = Field(default=None, primary_key=True)
    pedidos_id:int = Field(primary_key=True)
    produtos_id:int = Field(primary_key=True)
    quantidade:int = Field(index=False)
    preco:float = Field(index=False)
    pedidos_id:int = Field(foreign_key='pedidos.id')
    produtos_id:int = Field(foreign_key='produtos.id')

class Pagamentos(SQLModel, table=True):
    id:int |None = Field(default=None, primary_key=True)
    pedidos_id:int = Field(primary_key=True)
    valor:float = Field(index=False)
    metodo:str = Field(index=False)
    status:str = Field(index=False)
    criadoEm:datetime = Field(default_factory=datetime.utcnow)
    pedidos_id:int = Field(foreign_key='pedidos.id')

class Endereco(SQLModel, table=True):
    id:int |None = Field(default=None, primary_key=True)
    usuario_id:int = Field(primary_key=True)
    rua:str = Field(index=False)
    cidade:str = Field(index=False)
    estado:str = Field(index=False)
    cep:str = Field(index=False)
    usuario_id:int = Field(foreign_key='usuario.id')

class AValiacoes(SQLModel, table=True):
    id:int |None = Field(default=None, primary_key=True)
    usuario_id:int = Field(primary_key=True)
    produtos_id:int = Field(primary_key=True)
    nota:int = Field(index=False)
    comentario:str = Field(index=False)
    criadoEm:datetime = Field(default_factory=datetime.utcnow)
    usuario_id:int = Field(foreign_key='usuario.id')
    produtos_id:int = Field(foreign_key='produtos.id')

class Estoque(SQLModel, table=True):
    id:int |None = Field(default=None, primary_key=True)
    produtos_id:int = Field(primary_key=True, unique=True)
    quantidade:int = Field(index=False)
    atualizadoEm:datetime = Field(default_factory=datetime.utcnow)
    produtos_id: int = Field(foreign_key='produtos.id')
    