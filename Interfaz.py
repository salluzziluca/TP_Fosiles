from tkinter import *
import tkinter
from Constantes import *
from window import ventana_registro
from interfaz_de_registro import interfaz_registro, usuario_existente

def solicitar_nombre(dict_jugadores):
    #Hecho por Valentina Nieto y Camila Zarza, Oriz Omar, Luca Salluzzi,Agustín Conti,Lucas Osorio.
    #Solicita el ingreso de los nombres de los Jugadores
    raiz= Tk()
    raiz.title("Fosiles Memotest")
    raiz.resizable(0,0)
    #raiz.iconbitmap()
    raiz.geometry("400x600")
    raiz.config(bg="yellow")
    #frame
    miFrame=Frame(raiz)
    miFrame.pack(padx=10, pady=20)
    miFrame.config(cursor="heart")
    #jugadores j1
    usuario_existente=Label(miFrame, text="Usuario: ")
    usuario_existente.grid(row=0,column=0, padx=10, pady=10)
    usuario_var = StringVar()
    usuario_existente_entry=Entry(miFrame,textvariable=usuario_var)
    usuario_existente_entry.grid(row=0,column=1,padx=10, pady=10)
    #j2
    contraseña=Label(miFrame, text="Contraseña: ")
    contraseña.grid(row=1,column=0,padx=10, pady=10)
    contraseña_var = StringVar()
    contraseña_entry=Entry(miFrame,textvariable= contraseña_var)
    contraseña_entry.grid(row=1,column=1,padx=10, pady=10)
    contraseña_entry.config(show="*")
    #Mensaje login
    mensaje_login = Label(raiz, text = '')
    mensaje_login.config(bg = 'yellow',fg = 'black')
    mensaje_login.pack(padx= 50, pady=0)
    
    #Mensaje max jugadores 
    mensaje_jugadores = Label(raiz, text = f'El maximo total de jugadores es {MAX_JUGADORES}')
    mensaje_jugadores.config(bg = 'yellow',fg = 'black')
    mensaje_jugadores.pack(padx= 50, pady=0)
    
    #Listbox jugadores
    listbox_jugadores = Listbox(raiz)
    listbox_jugadores.pack()
    
    #funciones del boton
    def validaciones():
        usuarios_clave = open('usuarios.csv','r')
        linea = usuarios_clave.readline()
        linea = linea.rstrip('\n')
        registro = linea.split(',')
        valido = False
        while (not valido) and linea:
            if usuario_var.get() == registro[0] and contraseña_var.get() == registro[1]:
                valido = True
            else:
                linea = usuarios_clave.readline()
                registro = linea.split(',')
        usuarios_clave.close()
        return valido
    def presionar_enviar():
        # Valentina Nieto,Oriz Omar, Luca Salluzzi,Agustín Conti,Lucas Osorio.
        #No recibe nada. se ejecuta al presionar el Boton. Asigna el contenido de los entry al diccionario de jugadores. Cierra la interfaz.
        if len(dict_jugadores.keys())<= MAX_JUGADORES:
            if validaciones():
                dict_jugadores[usuario_var.get()] = [0,0]
                mensaje_login.config(bg='yellow',fg='black',text='Usuario ingresado correctamente')
                listbox_jugadores.insert(END, usuario_var.get())
            else:
                mensaje_login.config(bg='yellow',fg='black',text='Usuario y contraseña no coinciden con nuestros registros')
        else:
            raiz.destroy
        return None

    #Boton Envio
    boton_envio=Button(raiz, text="Logearse",command= presionar_enviar)
    boton_envio.pack()
    # Boton Registro
    boton_registro=Button(raiz, text="Registrarse",command= lambda: interfaz_registro(raiz))
    boton_registro.pack()
    #Boton Iniciar
    boton_inicio=Button(raiz, text="Iniciar Partida",command= raiz.destroy)
    boton_inicio.pack()
    raiz.mainloop()
    return None