class persona:
    def __init__(self,nombre, edad):
        self.nombre= nombre
        self.edad= edad

    def saludar(self):
        print("el nombre del estudiante es:", self.nombre ,"y la edad: ",self.edad)

class estudiante(persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado=grado
    def gradoestu(self):
        print("grado del estudiante es:" , self.grado)




maria= estudiante("maria",23,"primaria",)



maria.saludar()
maria.gradoestu()
