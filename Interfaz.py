from tkinter import *
from Constantes import ACIERTOS, INTENTOS

def solicitar_nombre(dict_jugadores):
    #Hecho por Valentina Nieto y Camila Zarza, Oriz Omar, Luca Salluzzi,Agustín Conti,Lucas Osorio.
    #Solicita el ingreso de los nombres de los Jugadores
    raiz= Tk()
    raiz.title("Fosiles Memotest")
    raiz.resizable(0,0)
    #raiz.iconbitmap()
    raiz.geometry("310x160")
    raiz.config(bg="yellow")
    #frame
    miFrame=Frame(raiz)
    miFrame.pack(padx=10, pady=20)
    miFrame.config(cursor="heart")
    #jugadores j1
    jugador_1=Label(miFrame, text="Primer Jugador: ")
    jugador_1.grid(row=0,column=0, padx=10, pady=10)
    nombre1_var = StringVar()
    jugador_1_entry=Entry(miFrame,textvariable=nombre1_var)
    jugador_1_entry.grid(row=0,column=1,padx=10, pady=10)
    #j2
    jugador_2=Label(miFrame, text="Segundo Jugador: ")
    jugador_2.grid(row=1,column=0,padx=10, pady=10)
    nombre2_var = StringVar()
    jugador_2_entry=Entry(miFrame,textvariable= nombre2_var)
    jugador_2_entry.grid(row=1,column=1,padx=10, pady=10)
    #funciones del boton
    def presionar_enviar():
        # Valentina Nieto,Oriz Omar, Luca Salluzzi,Agustín Conti,Lucas Osorio.
        #No recibe nada. se ejecuta al presionar el Boton. Asigna el contenido de los entry al diccionario de jugadores. Cierra la interfaz.
        dict_jugadores[nombre1_var.get()] = [0,0]
        dict_jugadores[nombre2_var.get()] = [0,0]
        raiz.destroy()
        return None
    #Boton
    Boton=Button(raiz, text="Enviar",command= presionar_enviar)
    Boton.pack()
    raiz.mainloop()
    return None
    
# LISTA TEMPORAL PARA TESTEO.
lista_jugadores_ordenada = [['Pedro',[3,9]],['Omar',[6,8]],['Agus',[7,6]],
                            ['Rogelio',[6,6]],['Pepe',[6,5]],['Rodolfo',[6,4]],
                            ['Julio',[6,3]],['Diego',[6,2]],['Fran',[6,1]],
                            ['Julio',[6,3]],['Diego',[6,2]],['Fran',[6,1]],
                            ['Julio',[6,3]],['Diego',[6,2]],['Fran',[6,1]],
                            ['Julio',[6,3]],['Diego',[6,2]],['Fran',[6,1]],
                            ]



#ranking_de_partida(lista_jugadores_ordenada,2)






# ACA PONEMOS LA FUNCION DE LA INTERFAZ Y LA IMPORTAMOS DESDE EL MAIN.
