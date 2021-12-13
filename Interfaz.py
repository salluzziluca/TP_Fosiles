from tkinter import *
from Constantes import MINIMO_JUGADORES
from Constantes_config import MAX_JUGADORES
from interfaz_de_registro import interfaz_registro

def validaciones(usuario, contraseña):
    #Desarollada por Luca Salluzzi
    #Valida si el usuario y la contraseña ingresadas corresponden con alguna linea del registro .csv
    usuarios_clave = open('usuarios.csv','r')
    linea = usuarios_clave.readline()
    linea = linea.rstrip('\n')
    registro = linea.split(',')
    valido = False
    while (not valido) and linea:
        if usuario == registro[0] and contraseña == registro[1]:
            valido = True
        else:
            linea = usuarios_clave.readline()
            linea = linea.rstrip('\n')
            registro = linea.split(',')
    usuarios_clave.close()
    return valido

def presionar_enviar(dict_jugadores, usuario, contraseña, listbox_jugadores, mensaje_login):
    # Valentina Nieto,Oriz Omar, Luca Salluzzi,Agustín Conti,Lucas Osorio.
    #Se ejecuta al presionar el Boton.Si el usuario y la contraseña coinciden con los registros, asigna el contenido de los entry al diccionario de jugadores y a la listbox presente en memoria, ademas notifica al usuario en ambos casos.
    
    if validaciones(usuario, contraseña):
        dict_jugadores[usuario] = [0,0]
        mensaje_login.config(bg = 'yellow',fg = 'black',text='Usuario ingresado correctamente')
        listbox_jugadores.insert(END, usuario)
            
    else:
        mensaje_login.config(bg = 'yellow',fg = 'black',text = 'Usuario y contraseña no coinciden con nuestros registros')
            
    return None

def verificar_cantidad_jugadores(dict_jugadores, boton_envio, boton_inicio):
    #Luca Salluzzi
    #Verifica si la cantidad de usuarios logeados (listos para jugar) es igual o mayor a la constante del archivo de configuración. 
    if len(dict_jugadores.keys()) >= (MAX_JUGADORES):
        boton_envio['state']='disabled'
    if len(dict_jugadores.keys()) >= MINIMO_JUGADORES:
        boton_inicio['state'] = 'active'
        
def solicitar_nombre(dict_jugadores):
    #Hecho por Valentina Nieto y Camila Zarza, Oriz Omar, Luca Salluzzi, Agustín Conti, Lucas Osorio.
    #Solicita el ingreso de los nombres de los Jugadores, muestra por pantalla el boton de registro, el de inicio de juego, el maximo de jugadores posibles, los nombres de los jugadores logueados y ademas, mensajes por pantalla del estado del login.
    raiz= Tk()
    raiz.title("Fosiles Memotest")
    raiz.resizable(0,0)
    
    #raiz.iconbitmap()
    raiz.geometry("400x450")
    raiz.config(bg="yellow")
    
    #frame
    miFrame=Frame(raiz)
    miFrame.pack(padx=10, pady=20)
    miFrame.config(cursor="heart")
    
    #casilla usario
    usuario_existente=Label(miFrame, text="Usuario: ")
    usuario_existente.grid(row=0,column=0, padx=10, pady=10)
    usuario_var = StringVar()
    usuario_existente_entry=Entry(miFrame,textvariable=usuario_var)
    usuario_existente_entry.grid(row=0,column=1,padx=10, pady=10)
    
    #casilla contraseña
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
    
    #Funcion deshabilitación del botón
   
            
    
    # Boton Registro
    boton_registro=Button(raiz, text ="Registrarse",command = lambda: interfaz_registro(raiz))
    boton_registro.pack()
    #Boton Iniciar
    boton_inicio=Button(raiz, text = "Iniciar Partida", state = DISABLED,command = raiz.destroy)
    boton_inicio.pack()

    #Boton Envio
    boton_envio=Button(raiz, text = "Logearse")
    boton_envio.configure(lambda:[presionar_enviar(dict_jugadores, usuario_var.get(), contraseña_var.get(), listbox_jugadores, mensaje_login), verificar_cantidad_jugadores(dict_jugadores, boton_envio, boton_inicio)])
    boton_envio.pack()
    raiz.mainloop()
    return None
