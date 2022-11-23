import json

class Controlador():
    def __init__(self):
        with open('controlador.json','r',encoding="UTF-8") as archivo:
            self.data = json.load(archivo)

    def cambiar_controlador_remoto(self):
        self.data['CONTROLADOR'] = "REMOTO"
        with open("controlador.json","w", encoding="UTF-8") as file:
            json.dump(self.data,file, indent=7)

    def cambiar_controlador_xpos(self):
        self.data['CONTROLADOR'] = "XPOS"
        with open("controlador.json","w", encoding="UTF-8") as file:
            json.dump(self.data,file, indent=7)

if __name__ == "__main__":
    llamar_controlador = Controlador()
    #llamar_controlador.cambiar_controlador_remoto()
    llamar_controlador.cambiar_controlador_xpos()
