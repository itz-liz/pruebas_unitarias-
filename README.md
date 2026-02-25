# pruebas_unitarias-
trabjo para aprender pruebas unitarias 
pytest -vv

#query  dividendo,divisor
1. def test division ():,
urls = f{Base_url}/divisiones
params ={"dividendo": "10", "divisor":"2"}
response = requests.get(url, params=params)
assert response status code == 200
data 1 ={
    "dividendo":10,
    "divisor":2,
    "division": 5
}

pasos para dseñar apis 
1. Diseñar la Api(endpoints)
2. Unit Test (pruebsas unitarias)
3. Codificacion 