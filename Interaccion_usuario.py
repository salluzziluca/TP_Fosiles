from Constantes import *
from Procesamiento_del_juego import validacion
import time

def mostrar_fichas(fichas):
    # Hecha por Luca Salluzzi, Omar, Lucas, Conti.
    # Muestra por pantalla (segun si la ficha esta o no dada vuelta) la letra o la posicion de la ficha. Luego, se ejecuta un salto de linea
    # cada cuarta posicion y al final del ciclo.
    n_posicion = 1
    contador=0
    for ficha in fichas:
        if contador==4:
            print('\n\n')
            contador=0
        if ficha[POSICION_BOOL]:
            print(f' {ficha[POSICION_LETRA]}', end='    ')
        else:
            if n_posicion < 10:                           # Condicionales para rectificar imagen de fichas en consola.
                print(f' {n_posicion}', end='    ')
            else:
                print(f'{n_posicion}', end='    ')
        n_posicion+=1
        contador+=1
    print('\n')
    return None

def input_usuario(fichas):
    # Hecha por Camila Zarza, Oriz.
    # Pide al usuario un ingreso numerico, devuelve ese numero.
    entero=False
    while not entero:
        try:
            input_realizado=int(input("Posición: "))
            if validacion(input_realizado,fichas):
                entero=True
            else:
                print('Número ingresado inválido.')
        except ValueError:
            print ('Valor inválido.')
        except TypeError:
            print ('Valor inválido.')
    return input_realizado

def mensaje_final(tiempo_inicial, resultado):
    # Hecha por Lucas Osorio, Omar Oriz y Agustin Conti.
    # Recibe el tiempo inicial e intentos e imprime el fin del juego con la cantidad de intentos y el tiempo empleado.
    print('Fin del juego!')
    print(f"\nEl juego duró {int(time.time() - tiempo_inicial)} segundos")
    if resultado != 'empate':
        print(f'\n{resultado}, Felicitaciones!\n')
    else:
        print(f'\nEl juego terminó en {resultado}')