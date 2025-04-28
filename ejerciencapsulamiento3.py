class Empleado:
def __init__(self, nombre, rol, clave):
self.__nombre = nombre
self.__rol = rol
self.__clave_acceso = self.__cifrar(clave)


def __cifrar (self, texto):
return texto[::-1]

def _descifrar(self, clave_encriptada):
return clave_encriptada[::-1]

@property
def nombre(self):
return self.__nombre
@property

def rol(self):
return self.__rol

def verificar_clave(self, clave_ingresada):
return self.__cifrar(clave_ingresada) == self.__clave_acceso

def cambiar_clave(self,clave_antigua, clave_nueva):
if self.verificar_clave(clave_antigua):
self.__clave_acceso = self.__cifrar
return True
return False

empl = Empleado("Andres","supervisor","hellokitty")
print(empl.verificar_clave("hellokitty"))
empl.cambiar_clave("hellokitty", "kdrama")

