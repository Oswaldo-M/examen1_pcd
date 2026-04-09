
class Revision:

    #Inicializa un nuevo producto 
    def __init__(self, id_revision,vehiculo,presion_bar,tipo_vehiculo):
        self.id_revision = id_revision
        self.vehiculo = vehiculo
        self.presion_bar = presion_bar
        self.tipo_vehiculo = tipo_vehiculo


    #Clasifica dependiendo del valor de la presion
    def clasificar(self):

        if self.presion_bar < 1.52:
            return "Muy baja"
        elif self.presion_bar < 2.07:
            return "Baja"
        elif self.presion_bar < 2.74:
            return "Normal"
        elif self.presion_bar < 3.62:
            return "Alta"
        else:
            return "Peligrosa"

    def __str__(self):
        return f"{self.id_revision} - {self.vehiculo} ({self.tipo_vehiculo}) - {self.presion_bar}"
    
    def __repr__(self):
        return f"Revision (id = '{self.id_revision}', valor = {self.presion_bar}, clase = '{self.clasificar()}')"