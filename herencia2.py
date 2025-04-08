class animal:
    def __init__(self,nombre, especie):
        self.nombre= nombre
        self.especie= especie

    def mostrar(self):
        print("el nombre del estudiante es:", self.nombre ,"y la especie: ",self.especie)

class perro(animal):
    def __init__(self, nombre, especie, raza):
        super().__init__(nombre, especie)
        self.raza=raza
    def raz(self):
        print("la raza del perro es:" , self.raza)


max= perro("max","canino","pastoer aleman")


max.mostrar()
max.raz()
