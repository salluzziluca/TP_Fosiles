from tkinter import*

def solicitar_nombre():
    #Solicita el ingreso de los nombres de los Jugadores
    #Hecho por Valentina Nieto y Camila Zarza
    raiz= Tk()
    raiz.title("Fosiles Memotest")
    raiz.resizable(0,0)
    #raiz.iconbitmap()
    raiz.geometry("300x150")
    raiz.config(bg="yellow")
    #frame
    miFrame=Frame(raiz)
    miFrame.pack(padx=10, pady=20)
    miFrame.config(cursor="heart")
    #jugadores j1
    jugador_1=Label(miFrame, text="Primer Jugador: ")
    jugador_1.grid(row=0,column=0, padx=10, pady=10)
    jugador_1_entry=Entry(miFrame)
    jugador_1_entry.grid(row=0,column=1,padx=10, pady=10)
    #j2
    jugador_2=Label(miFrame, text="Segundo Jugador: ")
    jugador_2.grid(row=1,column=0,padx=10, pady=10)
    jugador_2_entry=Entry(miFrame)
    jugador_2_entry.grid(row=1,column=1,padx=10, pady=10)
    #Boton
    Boton=Button(raiz, text="Enviar",command = lambda: acierto(jugador_1_entry.get(),jugador_2_entry.get()))
    Boton.pack()
    raiz.mainloop()
solicitar_nombre() 
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