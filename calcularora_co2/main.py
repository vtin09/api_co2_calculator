from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()


CO2_FACTORS = {
    "vidro": 0.315,
    "plástico": 1.5,
    "papel": 1.3,
    "papelão": 1.2,
    "madeira": 0.5,
    "orgânicos": 0.9,
    "fluidos de gás": 2.8,
}


class ReciclagemInput(BaseModel):
    material: str
    quantidade_kg: float
    



@app.post('/converter_co2')
def converter_co2(dados: ReciclagemInput):
    material = dados.material.lower()
    if material not in CO2_FACTORS:
        return{'erro': 'Desculpe, Material não reconhecido.'}
    
    fator = CO2_FACTORS[material]
    co2_evitado = dados.quantidade_kg * fator
    return {
        'material': material,
        'quantidade_kg': dados.quantidade_kg,
        'co2_evitado_kg': round(co2_evitado, 2)
    }
    