

#Valida que la presion sea numerica
def validar_presion(presion):
    try:
        presion = float(presion)
        return presion >= 0
    except (ValueError,TypeError):
        return False
    
#Valida que la unidad sea PSI o bar 
def validar_unidad(unidad):
    unidad = unidad.upper()
    if unidad not in ["PSI", "BAR"]:
        return False
    return True


#Valida cada dato
def validar_datos(id_revision,vehiculo,presion,unidad,tipo_vehiculo):
    
    if not id_revision or not str(id_revision).strip():
        return False, "id vacio o invalido"
    
    if not vehiculo or not str(vehiculo).strip():
        return False, "Vehiculo vacio o invalido"
    
    if not validar_presion(presion):
        return False, "Presion invalida"
    
    if not validar_unidad(unidad):
        return False, "Unidad invalida"
    
    if not tipo_vehiculo or not str(tipo_vehiculo).strip():
        return False, "Tipo de vehiculo vacio o invalido"
    
    return True, None


    