
from models.revision import Revision
from utils import leer_archivo,reporte_detalle,reporte_resumen
from utils import validar_datos,validar_unidad,validar_presion


ARCHIVO_ENTRADA = "datos/revisiones_neumaticos.csv"
ARCHIVO_REPORTE_DETALLE = "salidas/reporte_detalle.csv"
ARCHIVO_REPORTE_RESUMEN = "salidas/reporte_resumen.csv"


#Convierte la presion a bar 
def convertir_presion(datos_entrada):

    for dato in datos_entrada:
        #Valida si la presion se puede convertir a flo
        if validar_presion(dato["presion"]):
            #Convierte la presion a un valor flotante
            presionF = float(dato["presion"])
        #Ignora la linea si el valor en presion no es numerico
        else:
            continue
        
        #Se asegura que la unidad sea valida (PSI o bar)
        if validar_unidad(dato["unidad"].upper()):
            #Si la presion es PSI la convierte a bar 
            if dato["unidad"].upper() == "PSI":
                presion_bar = round(presionF * 0.0689,2)
            #Si la presion ya es bar la deja asi 
            else:
                presion_bar = round(presionF,2)
        #Ignora la linea cuando la unidad no es valida
        else:
            continue

        #Sobreescribe la clave "presion"
        dato["presion"] = presion_bar

    return datos_entrada


#Crea una lista de objetos tipo Revision
def crear_objetos(datos_revisados):
    #Crea lista de objetos tipo Revision
    datos_neumaticos = []

    #Valida si algun dato es invalido
    for dato in datos_revisados:
        valido, error = validar_datos(
            dato.get("id_revision"),
            dato.get("vehiculo"),
            dato.get("presion"),
            dato.get("unidad"),
            dato.get("tipo_vehiculo"),
        )

        #Ignora la linea con algun valor invalido
        if not valido:
            print(f"Ignorando reistro invalido - {error}")
            continue


        #Convierte el diccionario en un objeto Revision
        revision = Revision(id_revision=dato["id_revision"],vehiculo=dato["vehiculo"],
        presion_bar = dato["presion"],tipo_vehiculo=dato["tipo_vehiculo"]                        
        )
        #Añade el objeto Revision a la lista creada anteriormente
        datos_neumaticos.append(revision)

    return datos_neumaticos

#Ordena la lista por orden ascendente dependiendo del id revision
def ordenar_datos(datos_neumaticos):
    return sorted(datos_neumaticos, key=lambda dato: dato.id_revision)





def main():
    print("-"*50)
    print("Sistema de revision de presion de neumaticos")
    print("-" * 50)

    #Lee los datos
    print(f"Leyendo inventario de: {ARCHIVO_ENTRADA}")
    datos_entrada = leer_archivo(ARCHIVO_ENTRADA)
    

    #Convertir presion a unidad bar
    datos_revisados = convertir_presion(datos_entrada)

    #Crea objeto Revision
    datos_neumaticos = crear_objetos(datos_revisados)
    
    #Ordenar datos
    datos_neumaticos = ordenar_datos(datos_neumaticos)

    #Escribe el primer archivo de salida
    reporte_detalle(datos_neumaticos,ARCHIVO_REPORTE_DETALLE)
    print("Primer Archivo de salida generado")



if __name__ == "__main__":
    main()
        
    
