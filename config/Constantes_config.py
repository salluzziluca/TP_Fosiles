def leer_config():
    # Hecha por Conti 
    # Lee el csv de configuracion y retorna una tupla con lo que leyó
    config = open ("config/configuracion.csv", "r")
    variables = []
    linea = config.readline()
    linea = linea.replace(","," ").split()
    while linea:
        if linea[1].isnumeric():
            variables.append(int(linea[1]))
        elif linea[1] == "False":
            variables.append(False)
        elif linea[1] == "True":
            variables.append(True)
        linea = config.readline()
        linea = linea.replace(","," ").split()
        
    config.close()
    return tuple(variables)

# ARCHIVO DE CONFIG 
CANTIDAD_FICHAS, MAX_JUGADORES, MAX_PARTIDAS, REINICIAR_ARCHIVO_PARTIDAS = leer_config()

# POSICIONES
POSICION_LETRA = 0
POSICION_BOOL = 1
INGRESO1 = 0
INGRESO2 = 1

# CONSTANTES DE INICIALIZACION
INICIAR_CANT_PARTIDAS = 1

# CONSTANTES DEL CSV:
POS_NOMBRE_REGISTRO = 2
POS_ACIERTOS_REGISTRO = 3
POS_INTENTOS_REGISTRO = 4

# CONSTANTES DE POSICION DE DICCIONARIO
INTENTOS = 0
ACIERTOS = 1
PARTIDAS_JUGADAS = 2