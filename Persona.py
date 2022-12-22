class Persona:
    contador_persona = 0

    def __init__(self, nombre, edad):
        Persona.contador_persona += 1
        self.id_persona = Persona.contador_persona
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'


persona1 = Persona('Alejandro', 55)
print(persona1)

persona2 = Persona('Juan',30)
print(persona2)