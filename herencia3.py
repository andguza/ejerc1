class vehiculo:
    def __init__(self,marca, año):
        self.marca= marca
        self.año= año

    def vehi(self):
        print("la marca del vehiculo es:", self.marca ,"y el año: ",self.año)

class coche(vehiculo):
    def __init__(self, marca, año, modelo):
        super().__init__(marca, año)
        self.modelo=modelo
    def model(self):
        print("el modelo del vehiculo es:" , self.modelo)


mazda= coche("mazda",2025,"CX‑30")


mazda.vehi()
mazda.model()
