from os import stat
import random, time, datetime
from Constantes import *

def generar_fichas():
    # Hecha por Conti.
    # Genera una lista de fichas del tamaño puesto en la configuracion y las devuelve en posiciones aleatorias.
    lista_fichas = []
    caracteres_posibles = [chr(x) for x in range(65, 91)]
    while len(lista_fichas) < CANTIDAD_FICHAS:
        letra = caracteres_posibles.pop(random.randint(0, len(caracteres_posibles)-1))
        lista_fichas.append([letra, False])
        lista_fichas.append([letra, False])
    random.shuffle(lista_fichas)
    return lista_fichas

def elegir_primero(orden_jugadores):
    # Hecha por Oriz, Conti, Zarza, Osorio, Valen, Salluzzi
    # Elije el jugador que va a empezar aleatoriamente
    return random.choice(orden_jugadores)

def validacion(input_realizado,fichas):
    # Hecho por Omar Oriz.
    # recibe el input numérico del usuario y la lista de fichas actualizada, devuelve un bool
    # Dependiendo si es una pos correcta, y si la ficha no está boca arriba.
    return ((input_realizado-1) in range(len(fichas)) and fichas[input_realizado-1][POSICION_BOOL] != True)

def partida_completa(fichas):
    # Hecha por Agustín Conti
    # Determina si el juego terminó, comprobando que todas las fichas esten "volteadas".
    Terminado=True
    pos_maxima=len(fichas)-1
    pos_actual=0
    while Terminado and pos_actual <=pos_maxima:
        if not fichas[pos_actual][POSICION_BOOL]:
            Terminado=False
        pos_actual+=1    
    return Terminado

def voltear_ficha(lista_fichas,ingreso):
    # Hecha por Omar Oriz.
    # Recibe una lista de fichas y un input y devuelve la lista cambiada con la ficha (de pos. ingreso-1) volteada boca arriba.
    lista_fichas[ingreso-1][POSICION_BOOL]=True
    return None

def voltear_fichas_para_abajo(lista_fichas,ingresos):
    # Hecha por Omar Oriz.
    # Recibe una lista de fichas y una lista con ambos inputs del jugador y devuelve la lista de fichas con esas fichas boca abajo.
    lista_fichas[(ingresos[INGRESO1]-1)][POSICION_BOOL]=False
    lista_fichas[(ingresos[INGRESO2]-1)][POSICION_BOOL]=False
    return lista_fichas

def cambiar_jugador(jugador_anterior_pos,lista_jugadores):
    # Hecha por Oriz, Conti, Zarza, Osorio, Valen, Salluzzi
    # Devuelve el siguiente jugador en la lista de jugadores
    if jugador_anterior_pos != (len(lista_jugadores)-1):
        jugador_siguiente= lista_jugadores[jugador_anterior_pos+1]
    else:
        jugador_siguiente= lista_jugadores[0]
    
    return jugador_siguiente

def acierto(fichas, ingresos):
    # Hecha por Lucas Osorio y Valentina Nieto
    # Determina si el par de inputs ingresados en un turno es correcto, devuelve un booleano.
    return fichas[ingresos[INGRESO1]-1][POSICION_LETRA] == fichas[ingresos[INGRESO2]-1][POSICION_LETRA]

def timer_delay(segundos):
    # Omar Oriz
    # Genera un delay de la cantidad de segundos pedida, en la que se "frena" el avance del programa.
    t_inicial = time.time()
    tiempo_transcurrido = 0
    while tiempo_transcurrido < segundos:
        t_actual = time.time()
        tiempo_transcurrido = t_actual - t_inicial
    return None

def juntar_datos_partida(dict_jugadores,dict_jugadores_total):
    # Hecha por Omar Oriz, Agustin Conti.
    # recibe diccionario de jugadores de cada partida y un diccionario que almacena los datos de todas las partidas.
    # Actualiza el segundo en base al primero.
    for jugador, stats in dict_jugadores.items():

        if jugador not in dict_jugadores_total:
            dict_jugadores_total[jugador] = stats
        else:
            dict_jugadores_total[jugador][INTENTOS] += stats[INTENTOS]
            dict_jugadores_total[jugador][ACIERTOS] += stats[ACIERTOS]
    

def guardar_partida_en_csv(dict_jugadores_ordenado):
    # hecha por Omar Oriz, Agustin conti.
    # Recibe el diccionario de jugadores de cada partida y registra sus datos en el csv de ranking all-time.
    fecha_actual = datetime.datetime.now().strftime("%x")
    hora_actual = datetime.datetime.now().strftime("%X")
    archivo = open('historial_all_time.txt', 'a')  # a de append para no pisar.
    for jugador, stats in dict_jugadores_ordenado:
        archivo.write(f'{fecha_actual},{hora_actual},{jugador},{stats[ACIERTOS]},{stats[INTENTOS]}\n')
    archivo.close()