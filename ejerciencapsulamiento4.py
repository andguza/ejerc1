class Persona:
    def __init__(self, nombre, edad, documento):
        self.__nombre = nombre
        self.__documento = documento
        self.__edad = None
        self.edad = edad  # Usando el setter para validar la edad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if valor >= 0:
            self.__edad = valor
        else:
            raise ValueError("La edad no puede ser negativa.")

    @property
    def documento(self):
        return self.__documento


class Paciente(Persona):
    def __init__(self, nombre, edad, documento, diagnostico):
        super().__init__(nombre, edad, documento)
        self.__diagnostico = diagnostico
        self.__historial = []

    def agregar_historial(self, entrada):
        self.__historial.append(entrada)

    def ver_historial(self):
        return self.__historial

    def ver_diagnostico(self):
        return self.__diagnostico


class Doctor(Persona):
    def __init__(self, nombre, edad, documento, especialidad):
        super().__init__(nombre, edad, documento)
        self.__especialidad = especialidad

    def ver_especialidad(self):
        return self.__especialidad

    def modificar_diagnostico(self, paciente, nuevo_diagnostico):
        if isinstance(paciente, Paciente):
            paciente._Paciente__diagnostico = nuevo_diagnostico
            return f"Diagnóstico actualizado a: {nuevo_diagnostico}"
        return "La modificación solo puede hacerse a instancias de Paciente."


# Ejemplo de uso:
paciente1 = Paciente("Maria", 25, "110225514", "Resfriado")
doctor1 = Doctor("Dr. Luis", 40, "852668", "Cardiología")

print(paciente1.ver_diagnostico())
doctor1.modificar_diagnostico(paciente1, "Neumonía")
print(paciente1.ver_diagnostico())
paciente1.agregar_historial("Consulta realizada el 28 de abril")
print(paciente1.ver_historial())