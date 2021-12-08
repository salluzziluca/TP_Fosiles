from tkinter import *

from window import ventana_registro
from interfaz_de_registro import interfaz_registro

def solicitar_nombre(dict_jugadores):
    #Hecho por Valentina Nieto y Camila Zarza, Oriz Omar, Luca Salluzzi,Agustín Conti,Lucas Osorio.
    #Solicita el ingreso de los nombres de los Jugadores
    raiz= Tk()
    raiz.title("Fosiles Memotest")
    raiz.resizable(0,0)
    #raiz.iconbitmap()
    raiz.geometry("400x200")
    raiz.config(bg="yellow")
    #frame
    miFrame=Frame(raiz)
    miFrame.pack(padx=10, pady=20)
    miFrame.config(cursor="heart")
    #jugadores j1
    jugador_1=Label(miFrame, text="Usuario: ")
    jugador_1.grid(row=0,column=0, padx=10, pady=10)
    nombre1_var = StringVar()
    jugador_1_entry=Entry(miFrame,textvariable=nombre1_var)
    jugador_1_entry.grid(row=0,column=1,padx=10, pady=10)
    #j2
    contraseña=Label(miFrame, text="Contraseña: ")
    contraseña.grid(row=1,column=0,padx=10, pady=10)
    nombre2_var = StringVar()
    contraseña_entry=Entry(miFrame,textvariable= nombre2_var)
    contraseña_entry.grid(row=1,column=1,padx=10, pady=10)
    contraseña_entry.config(show="*")
    #funciones del boton
    def presionar_enviar():
        # Valentina Nieto,Oriz Omar, Luca Salluzzi,Agustín Conti,Lucas Osorio.
        #No recibe nada. se ejecuta al presionar el Boton. Asigna el contenido de los entry al diccionario de jugadores. Cierra la interfaz.
        dict_jugadores[nombre1_var.get()] = [0,0]
        return None
    #Boton Envio
    boton_envio=Button(raiz, text="Logearse",command= presionar_enviar)
    boton_envio.pack()
    # Boton Registro
    boton_registro=Button(raiz, text="Registrarse",command= interfaz_registro)
    boton_registro.pack()
    #Boton Iniciar
    boton_inicio=Button(raiz, text="Iniciar Partida",command= raiz.destroy)
    boton_inicio.pack()
    raiz.mainloop()
    return None
    


# ACA PONEMOS LA FUNCION DE LA INTERFAZ Y LA IMPORTAMOS DESDE EL MAIN.
