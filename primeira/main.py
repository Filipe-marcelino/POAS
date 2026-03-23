#pip install fastapi uvicorn
#uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'mensagem' : 'Olá'}

