
"""
def mostrar_las_fichas(fichas):
    #Muestra por pantalla (segun si la ficha esta o no dada vuelta) la letra o la posicion de la ficha.
    #hecho por Luca Salluzzi, O.Oriz.
    n_posicion=1
    for ficha in fichas:

        if ficha[POSICION_BOOL]:
            print(f'[{ficha[POSICION_LETRA]}]', end=' ')
        else:
            print(f'[{n_posicion}]', end=' ')
        n_posicion+=1
    print('\n')
mostrar_las_fichas(lista_prueba)
"""


"""fichas =[["D",False],["D",False],["s",False],["s",False]]
ingresos = [3,2]
def acierto(fichas, ingresos):
    # Determina si el par de inputs ingresados en un turno es correcto, devuelve un booleano.
    # Hecha por
    if fichas[ingresos[INGRESO1]-1][POSICION_LETRA] == fichas[ingresos[INGRESO2]-1][POSICION_LETRA]:
        verificar = True
    else:
        verificar = False
    
    return verificar
    
"""
"""
def voltear_ficha_para_abajo(fichas,ingresos):

    fichas[(ingresos[INGRESO1]-1)][POSICION_BOOL]=False
    fichas[(ingresos[INGRESO2]-1)][POSICION_BOOL]=False
    return fichas
"""


################################################################### BOCETO VALIDACION ##################
"""
def input_usuario(fichas2):
    # Pide al usuario un ingreso numerico, devuelve ese numero.
    # Hecha por Camila Zarza, Oriz.
    entero=False
    while not entero:
        try:
            posicion=int(input("Posición: "))
            if validacion(posicion,fichas2):
                entero=True
        except ValueError:
            print ('Valor inválido.')
        except TypeError:
            print ('Valor inválido.')
    return posicion

def validacion(input_realizado,fichas):
    #recibe el input numérico del usuario y la lista de fichas actualizada, devuelve un bool
    # Dependiendo si es una pos correcta, y si la ficha no está boca arriba.
    # Hecho por Omar Oriz.
    return ((input_realizado-1) in range(len(fichas)-1) and fichas[input_realizado-1][POSICION_BOOL] != True)

        
            
def turno(fichas):
    # Define una ronda de selección de fichas. Devuelve la lista con el par de ELECCIONES y los ingresos realizados.
    # Hecha por Oriz, Conti, Zarza.
    fichas2=fichas
    n=0
    print('Nuevo turno, Sus fichas:')
    mostrar_fichas(fichas)
    ingresos=[]
    while n<2:
        input1=input_usuario(fichas2)
        ingresos.append(input1)
        fichas2=cambiar(fichas2,input1)
        mostrar_fichas(fichas2)

        n+=1

    return fichas2,ingresos
"""
#############################################################################################
