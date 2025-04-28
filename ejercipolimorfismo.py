class transporte:
def tipo_transporte(self):
pass

class coche(transporte):
def tipo_transporte (self):
return "terrestre"

class avion(transporte):
def tipo_transporte (self):
return "aereo"


class barco(transporte):
def tipo_transporte (self):
return "maritimo"


coche = coche()
print("Coche es tipo: ",coche.tipo_transporte())
avion = avion()
print("Avion es tipo: ",avion.tipo_transporte())
barco = barco()
print( "Barco es tipo: ", barco.tipo_transporte())