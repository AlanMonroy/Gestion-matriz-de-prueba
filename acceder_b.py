import json

def conectar_controlador_json():
    try:
        while True:
            with open('controlador.json','r',encoding="UTF-8") as archivo:
                data = json.load(archivo)
                if data["CONTROLADOR"] == "XPOS":
                    print("XPOS")
                elif data["CONTROLADOR"] == "REMOTO":
                    print("REMOTO")
    except Exception as e:
        conectar_controlador_json()

conectar_controlador_json()