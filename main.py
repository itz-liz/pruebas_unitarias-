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

def test_division0():
    urls = f"{Base_url}/divisiones"
    params = {"dividendo": "10", "divisor": "0"}
    response = requests.get(urls, params=params)
    assert response.status_code == 400
    data2={
        "dividendo":10,
        "divisor":0,
        "division": "Error: No se puede dividir por cero"
    }
assert response.json() == data2

def test_division_negativo():
    urls = f"{Base_url}/divisiones"
    params = {"dividendo": "-10", "divisor": "2"}
    response = requests.get(urls, params=params)
    assert response.status_code == 200
    data3={
        "dividendo":-10,
        "divisor":2,
        "division": -5
    }
assert response.json() == data3

def test_division_negativo2():
    urls = f"{Base_url}/divisiones"
    params = {"dividendo": "10", "divisor": "-2"}
    response = requests.get(urls, params=params)
    assert response.status_code == 200
    data4={
        "dividendo":10,
        "divisor":-2,
        "division": -5
    }
assert response.json() == data4
# test_restas utilizado path parameters
def test_restas():
    urls = f"{URL_BASE}/restas/10/2"
    response = requests.get(urls)
    assert response.status_code == 200
    assert response.json() == {
        "numero1": 10,
        "numero2": 2,
        "resta": 8
    }    

# test_multiplicaciones utilizando post con body 
def test_multiplicaciones():
    url = f"{URL_BASE}/multiplicaciones"
    data = {"numero1": 4, "numero2": 5}
    response = requests.post(url, json=data)
    assert response.status_code == 202
    assert response.json() == {
        "numero1": 4,
        "numero2": 5,
        "multiplicacion": 20
    }

