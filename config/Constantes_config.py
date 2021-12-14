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
        elif linea[1] == "False" :
            variables.append(False)
        elif linea[1] == "True":
            variables.append(True)
        linea = config.readline()
        linea = linea.replace(","," ").split()
        
    config.close()
    return tuple(variables)

# ARCHIVO DE CONFIG 
CANTIDAD_FICHAS, MAX_JUGADORES, MAX_PARTIDAS, REINICIAR_ARCHIVO_PARTIDAS = leer_config()