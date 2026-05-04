from sqlmodel import SQLModel, Field

class Usuario(SQLModel, table=True):
    id:int |None = Field(default=None, primary_key=True)
    nome:str = Field(index=False)
    email:str = Field(index=False)
    senha:hash = Field(index=False)

class Papeis(SQLModel, table=True):
    id:int |None = Field(default=None, primary_key=True)
    nome:str = Field(index = False)