
from models.revision import Revision
from utils import leer_archivo,reporte_detalle,reporte_resumen
from utils import validar_datos,validar_unidad,validar_presion

#Configuracion
ARCHIVO_ENTRADA = "datos/revisiones_neumaticos.csv"
ARCHIVO_REPORTE_DETALLE = "salidas/reporte_detalle.csv"
ARCHIVO_REPORTE_RESUMEN = "salidas/reporte_resumen.csv"


#Convierte la presion a bar 
def convertir_presion(datos_entrada):
    #Lista donde de adjuntan las lineas validas
    datos_validos= []
    for dato in datos_entrada:
        #Valida si la presion se puede convertir a flo
        if validar_presion(dato["presion"]):
            #Convierte la presion a un valor flotante
            presionF = float(dato["presion"])
        #Ignora la linea si el valor en presion no es numerico
        else:
            continue
        
        #Se asegura que la unidad sea valida (PSI o bar)
        if validar_unidad(dato["unidad"]):
            #Si la presion es PSI la convierte a bar 
            if dato["unidad"] == "PSI":
                presion_bar = round(presionF * 0.0689,2)
            #Si la presion ya es bar la deja asi 
            else:
                presion_bar = round(presionF,2)
        #Ignora la linea cuando la unidad no es valida
        else:
            continue

        #Sobreescribe la clave "presion"
        dato["presion"] = presion_bar
        datos_validos.append(dato)

    return datos_validos


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



#Crea un diccionario para la segunda salida
def crear_dic(datos_revisados):
    #Inicializa diccionario
    datos_conteo = {}


    for dato in datos_revisados:
        #Si el tipo de vehiculo no esta en el diccionario lo crea e inicializa
        if dato["tipo_vehiculo"] not in datos_conteo:
            datos_conteo[dato["tipo_vehiculo"]] = {
                "conteo":0,
                "suma": 0.0,
                "maximo":0
            }
        #Realiza el conteo de los tipos de vehiculos
        datos_conteo[dato["tipo_vehiculo"]]["conteo"] += 1
        #Va sumando la presion 
        datos_conteo[dato["tipo_vehiculo"]]["suma"] += dato["presion"]

        #Va encontrando el maximo de cada tipo de vehiculo
        if dato["presion"] > datos_conteo[dato["tipo_vehiculo"]]["maximo"]:
            datos_conteo[dato["tipo_vehiculo"]]["maximo"] = dato["presion"]

    
    for tipo in datos_conteo:
        conteo = datos_conteo[tipo]["conteo"]
        suma = datos_conteo[tipo]["suma"]
        #Encuentra el promedio de presion de cada tipo de vehiculo
        datos_conteo[tipo]["promedio"] = suma/conteo if conteo > 0 else 0 
        
    #Retorna el diccionario con todos los tipos de vehiculos y los valores correspondientes
    return datos_conteo 

#Ordena el diccionario para la segunda salida
def ordenar_dic(datos_conteo):

    #Ordena por tipo de vehiculo en orden alfabetico
    ord1 = sorted(datos_conteo.items(), key=lambda d: d[0])
    
    #Ordena por valor de conteo de manera descendente
    ord2= sorted(ord1, key=lambda d: d[1]["conteo"],reverse=True) 
    
    #Convierte a diccionario y retorna 
    return dict(ord2)


def main():
    print("-"*50)
    print("Sistema de conversion de presion de neumaticos")
    print("-" * 50)

    #Lee los datos
    print(f"Leyendo inventario de: {ARCHIVO_ENTRADA}")
    datos_entrada = leer_archivo(ARCHIVO_ENTRADA)
    

    #Convertir presion a unidad bar
    datos_revisados = convertir_presion(datos_entrada)

    #Creando diccionario para la segunda salida
    datos_conteo = crear_dic(datos_revisados)

    #Ordenar el diccionario para la segunda salida
    datos_conteo = ordenar_dic(datos_conteo)
    
    #Crea objeto Revision 
    datos_neumaticos = crear_objetos(datos_revisados)
    
    #Ordenar datos de la primera salida
    datos_neumaticos = ordenar_datos(datos_neumaticos)

    #Escribe el primer archivo de salida
    reporte_detalle(datos_neumaticos,ARCHIVO_REPORTE_DETALLE)
    print("Primer Archivo de salida generado")

    #Escribe el segundo archivo de salida
    reporte_resumen(datos_conteo,ARCHIVO_REPORTE_RESUMEN)
    print("Segundo archivo de salida generado")

    print("-"*50)
    print("Proceso finalizado con exito")
    print("-"*50)


if __name__== "__main__":
    main()
        
    
