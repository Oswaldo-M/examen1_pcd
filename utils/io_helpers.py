

#Funcion para leer el archivo de entrada
def leer_archivo(archivo_entrada):

    #Lista vacia donde se almacenaran los registros validos
    datos = []

    with open(archivo_entrada, 'r', encoding= 'utf-8') as archivo:
        lineas = archivo.readlines()

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








