class MiClase:

    variable_clase = 'valor variable de clase '

    def __init__(self,variable_instancia):
        self.variable_instancia = variable_instancia

print (MiClase.variable_clase)
miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)