
from models.revision import Revision
from utils import leer_archivo,reporte_detalle,reporte_resumen
from utils import validar_datos,validar_unidad,validar_presion


ARCHIVO_ENTRADA = "datos/revisiones_neumaticos.csv"
ARCHIVO_REPORTE_DETALLE = "salidas/reporte_detalle.csv"
ARCHIVO_REPORTE_RESUMEN = "salidas/reporte_resumen.csv"





def convertir_presion(datos_entrada):

    for dato in datos_entrada:
        
        #Convierte la presion a flotante
        try:
            presionF = float(dato["presion"])
        #Ignora la linea si presion no es un valor numerico
        except (ValueError,TypeError,KeyError):
            continue
        
        #Se asegura que la unidad sea valida (PSI o bar)
        if validar_unidad(dato["unidad"].upper()):
            #Si la presion es PSI la convierte a bar 
            if dato["unidad"].upper() == "PSI":
                presion_bar = presionF * 0.0689
            #Si la presion ya es bar la deja asi 
            else:
                presion_bar = presionF
        #Ignora la linea cuando la unidad no es valida
        else:
            continue

        #Sobreescribe la clave "presion"
        dato["presion"] = presion_bar
        
    return datos_entrada



def crear_objetos(datos_entrada):
    datos_neumaticos = []

    for dato in datos_entrada:
        valido, error = validar_datos(
            dato.get("id_revision"),
            dato.get("vehiculo"),
            dato.get("presion"),
            dato.get("unidad"),
            dato.get("tipo_vehiculo"),
        )

        if not valido:
            print(f"Ignorando reistro invalido - {error}")
            continue

        revision = Revision(id_revision=dato["id_revision"],vehiculo=dato["vehiculo"],
        presion_bar = dato["presion"]                        
        )



        
        
    
