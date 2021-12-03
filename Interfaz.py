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


def ranking_de_partida(lista_jugadores_ordenada,partidas_jugadas,juego_terminado):

    def coordinar_scroll_con_frame(lienzo):
        # resetear la region de scroll para encompazar el frame
        lienzo.configure(scrollregion=lienzo.bbox("all"))

    def poblar_frame(frame_ranking,lista_jugadores_ordenada,trofeo_ganador):
        # Recibe el frame, la lista de j. ordenada y la imagen trofeo. Se encarga de mostrar en la interfaz la tabla de ranking 
        # con todas sus estadísticas.
        #---------------------------------- label fijos--------------------------------------------
        espacio = Label(frame_ranking,text='            ',bg='thistle2',pady=15,padx=10)
        espacio.grid(column=0,row=0)

        nombre_jugador = Label(frame_ranking,text='Nombre del Jugador',font=("Bahnschrift", 15),bg = 'thistle2', borderwidth="1",pady=15,padx=10)
        nombre_jugador.grid(column=1,row=0)

        aciertos_jugador = Label(frame_ranking,text='Aciertos',font=("Bahnschrift", 15),bg = 'thistle2', borderwidth="1",pady=15,padx=10)
        aciertos_jugador.grid(column=3,row=0)

        intentos_jugador = Label(frame_ranking,text='Intentos',font=("Bahnschrift", 15),bg = 'thistle2', borderwidth="1",pady=15,padx=10)
        intentos_jugador.grid(column=5,row=0)

        promedio_intentos_jugador = Label(frame_ranking,text='Promedio de intentos',font=("Bahnschrift", 15),bg = 'thistle2', borderwidth="1",pady=15,padx=10)
        promedio_intentos_jugador.grid(column=7,row=0)

        trofeo = Label(frame_ranking,image= trofeo_ganador,bg= 'thistle2',height=77,width=88)
        trofeo.grid(column= 0,row= 1)

        #---------------------------------- label generados--------------------------------------------
        columna_actual = 1
        fila_actual = 1
        lugar = 2
        tamanio_letra = 30
        for jugador,estadisticas in lista_jugadores_ordenada:

            if columna_actual == 0:
                temp_label = Label(frame_ranking,text=f'{lugar}º',font=("Bahnschrift", tamanio_letra),bg = 'thistle2', borderwidth="1",relief="solid")
                temp_label.grid(column= columna_actual , row= fila_actual)
                columna_actual +=1
                lugar += 1 

            temp_label = Label(frame_ranking,text=f'{jugador}',font=("Bahnschrift", tamanio_letra),bg = 'thistle2')
            temp_label.grid(column= columna_actual , row= fila_actual)

            temp_label = Label(frame_ranking,text=f'{estadisticas[ACIERTOS]}',font=("Bahnschrift", tamanio_letra),bg = 'thistle2')
            temp_label.grid(column= columna_actual+2 , row= fila_actual)

            temp_label = Label(frame_ranking,text=f'{estadisticas[INTENTOS]}',font=("Bahnschrift", tamanio_letra),bg = 'thistle2')
            temp_label.grid(column= columna_actual+4 , row= fila_actual)

            temp_label = Label(frame_ranking,text=f'{estadisticas[INTENTOS]/partidas_jugadas}',font=("Bahnschrift", tamanio_letra),bg = 'thistle2')
            temp_label.grid(column= columna_actual+6 , row= fila_actual)
            if tamanio_letra > 10:
                tamanio_letra -=3
            fila_actual += 1
            columna_actual = 0
        return fila_actual

    def boton_salir():
        nonlocal juego_terminado
        juego_terminado = True
        
        raiz_ranking.destroy()

    #---------------------------------- raíz--------------------------------------------
    raiz_ranking = Tk()
    raiz_ranking.title("Ranking de partida")
    raiz_ranking.attributes('-topmost', True)
    raiz_ranking.resizable(0,0)
    raiz_ranking.geometry("720x400")
    raiz_ranking.config(bg="thistle2")
    #---------------------------------- Scroll--------------------------------------------
    barra_scroll = Scrollbar(raiz_ranking,orient="vertical",)
    #---------------------------------- Lienzo--------------------------------------------
    lienzo = Canvas(raiz_ranking)
    #---------------------------------- frame--------------------------------------------
    frame_ranking = Frame(lienzo)
    frame_ranking.config(bg='thistle2')
    #---------------------------------- Configuracion del scroll--------------------------------------------
    barra_scroll.config(command=lienzo.yview)
    barra_scroll.pack(side="right", fill="y")

    #---------------------------------- Configuracion del lienzo--------------------------------------------
    lienzo.configure(yscrollcommand=barra_scroll.set, bg = 'thistle2') # parametro de configuracion yscrollcommand seteando la  barra_scroll como scroller.
    lienzo.pack(side="left", fill="both", expand=True)
    lienzo.create_window((0,0), window=frame_ranking, anchor="n")

    #---------------------------------- relacionar el frame con la barra de scroll.--------------------------------------------
    frame_ranking.bind("<Configure>", lambda event, lienzo=lienzo: coordinar_scroll_con_frame(lienzo))
    #---------------------------------- Imagenes --------------------------------------------
    trofeo_ganador = PhotoImage(file='trofeo_ganador.png')
    #---------------------------------- Poblar Frame --------------------------------------------
    ultima_fila = poblar_frame(frame_ranking,lista_jugadores_ordenada,trofeo_ganador)

    #---------------------------------- Botones --------------------------------------------

    fila_actual = ultima_fila+1
    salir_del_juego = Button(frame_ranking,text='Salir del juego',command = boton_salir , bg = 'pale violet red',fg = 'dark slate blue',activebackground='violetred3' )
    salir_del_juego.grid(column = 1,row = fila_actual,pady=10)

    nueva_partida = Button(frame_ranking,text='Nueva Partida',command = raiz_ranking.destroy ,bg = 'medium sea green',fg = 'dark slate blue',activebackground = 'sea green')
    nueva_partida.grid(column = 7,row = fila_actual,pady=10)


    raiz_ranking.mainloop()


#ranking_de_partida(lista_jugadores_ordenada,2)






# ACA PONEMOS LA FUNCION DE LA INTERFAZ Y LA IMPORTAMOS DESDE EL MAIN.
