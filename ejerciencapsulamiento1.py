class Estudiante:
def __init__(self, nombre, codigo):
self.__nombre = nombre
self.__codigo = codigo
self.__notas = []



@property
def nombre(self):
return self.__nombre


@nombre.setter
def nombre(self, valor):
if not valor.strip():
raise ValueError("El nombre no puede estar vacío.")
self.__nombre = valor
@property
def codigo(self):
return self.__codigo

@codigo.setter
def codigo(self, valor):
if not valor.isalnum():
raise ValueError("El código debe ser alfanumérico.")
self.__codigo = valor

def agregar_nota(self, nota):
if 0.0 <= nota <= 5.0:
self.__notas.append(nota)
else:
raise ValueError("La nota debe estar entre 0.0 y 5.0.")

def calcular_promedio(self):
if not self.__notas:
return 0.0
return sum(self.__notas) / len(self.__notas)

def es_aprobado(self):
return self.calcular_promedio() >= 3.0


# Crear una instancia de la clase Estudiante
estudiante = Estudiante("Juan Pérez", "A12345")

# Establecer nombre y código
estudiante.nombre = "Juan Pérez"
estudiante.codigo = "A12345"

# Agregar notas válidas
estudiante.agregar_nota(1.0)
estudiante.agregar_nota(3.5)
estudiante.agregar_nota(2.8)

# Calcular el promedio y verificar si está aprobado
promedio = estudiante.calcular_promedio()
estado = estudiante.es_aprobado()

# Mostrar resultados
print("Nombre:", estudiante.nombre)
print("Código:", estudiante.codigo)
print("Promedio de notas:", promedio)
print("¿Está aprobado?:", estado)