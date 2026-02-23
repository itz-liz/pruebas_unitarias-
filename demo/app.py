import requests
import json
import time
import random 

url = "https://iot345-default-rtdb.firebaseio.com/sensores/sucursal1.json"

def enviar_datos():
    response = requests.get(url)
    print (response.status_code)
    print (response.text)

def simular_sensores():
    while True:
        data = {
            "temperatura": random.randint(0, 100),
            "humedad": random.randint(0, 100),
        }
        response = requests.put(url, data=json.dumps(data))
        print (response.status_code)
        print (response.text)
        time.sleep(1)

if __name__ == "__main__":
    #enviar_datos()
    simular_sensores()