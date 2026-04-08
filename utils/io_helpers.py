

#Funcion para leer el archivo de entrada
def leer_archivo(archivo_entrada):

    #Lista vacia donde se almacenaran los registros validos
    datos = []

    with open(archivo_entrada, 'r', encoding= 'utf-8') as entrada:
        lineas = entrada.readlines()

        #Si el archivo esta vacio devuele la lista "datos" vacia
        if not lineas:
            return datos
        
        #Obtiene los encabezados del archivo
        encabezados = lineas[0].strip().split(',')

        #Lee cada linea a partir de la segunda
        for linea in lineas[1:]:

            #Ignora lineas vacias
            if not linea:
                continue
            
            
            valores = linea.strip().split(',')
            
            #Ignora lineas con numero incorrecto de columnas 
            if len(valores) != len(encabezados):
                continue
            
            #Genera un diccionario con los encabezados y los valores obtenidos de cada linea
            dato_dic = dict(zip(encabezados,valores))

            #Añade el diccionario de cada linea a la lista "datos"
            datos.append(dato_dic)

    return datos

def reporte_detalle(datos_ordenados,ruta_archivo):

    encabezados= ["id_revision","vehiculo","tipo_vehiculo","presion_bar","estado_presion"]

    with open(ruta_archivo, 'w', encoding= 'utf-8') as archivo:
        #Escribir los encabezados
        archivo.write(','.join(encabezados) + '\n')

        #Escribir datos
        for dato in datos_ordenados:
            linea = f"{dato.id_revision},{dato.vehiculo},{dato.tipo_vehiculo},"
            linea +=f"{dato.presion_bar:.2f},{dato.clasificacion()}"
            archivo.write(linea + '\n') 


def reporte_resumen(datos_dic,ruta_archivo):
    encabezados = ["tipo_vehiculo","conteo","promedio","maximo"]


    with open(ruta_archivo,'w',encoding='utf-8') as archivo:
        #Escrbir los encabezados
        archivo.write(','.join(encabezados) + '\n')

        #Desempaquetando y escribiendo los datos
        for tipo,dato in datos_dic.items():
            linea = f"{tipo},{dato['conteo']},{dato['promedio']},{dato['maximo']}"
            archivo.write(linea + '\n')





