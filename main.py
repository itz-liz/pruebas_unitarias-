from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def get_root():
    data = {"message":"Pruebas unitarias"}
    return JSONResponse(content=data, status_code=202)


@app.get("/sumas")
def sumas(numero1: int=0, numero2: int=0):
    suma = numero1 + numero2
    data = {"numero1": numero1,
            "numero2": numero2,
            "suma": suma
    }
    return JSONResponse(content=data, status_code=202)

def test_division():
    urls = f"{Base_url}/divisiones"
    params = {"dividendo": "10", "divisor": "2"}
    response = requests.get(urls, params=params)
    assert response.status_code == 200
    data1 = {
    "dividendo":10,
    "divisor":2,
    "division": 5
}
assert response.json() == data1

