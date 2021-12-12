from tkinter import *
import csv
def ventana_registro():
  ventana = Tk()
  ventana.geometry("800x500")
  ventana.title("Registro | Login CSV")
  #vale
  def lectura_usuarios():
    #Valentina Nieto
    # Lista con el contenido del archivo
    usuarios = []
    # Abrir el archivo usuarios.csv, tener en cuenta la ruta del archivo.
    with open('usuarios.csv') as f:
      # Leer el archivo al iniciar el programa
      reader = csv.reader(f)
      # Recorrer y agregar a la lista el contenido del archivo
      for row in reader:
        usuarios.append(row)
      # Cerrar lectura
      f.close()
    return usuarios
  def user_register(usuarios):
    #vale
    # agrega el nombre y la contraseña a un objeto para concatenarlo a la lista de usuarios en el archivo
    new_user = [user_name.get(), password.get()]

    # Abrir el archivo usuarios.csv, tener en cuenta la ruta del archivo.
    with open('usuarios.csv') as f:
      reader = csv.reader(f)

      # Recorrer el contenido del archivo
      registrado = False
      for row in reader:

        # Valida si el usuario que estan ingresando ya esta registrado, si si, termina la función
        if user_name.get() == row[0] and password.get() == row[1]:
          registrado = True
  
      if registrado == False:
        usuarios.append(new_user)
        print("Usuario nuevo registrado.")
      else:
        print('el usuario ya se encuentra registrado')
      
    # Cerrar lectura
    f.close()

    # Abrir el archivo usuarios.csv con permisos de escritura(w), tener en cuenta la ruta del archivo.
    with open('usuarios.csv', 'w') as f:
      writer = csv.writer(f, delimiter=",")
      # Agregar al archivo la lista que se genera en usuarios
      writer.writerows(usuarios)
    
    # Cerrar lectura
    f.close()

  def log_in(usuarios):
    #vale
    # Variable booleana para validar login
    login = False

    # Recorrer la lista con el contenido del archivo generado
    for i in usuarios:
      # Validar el user name del usuario
      if user_name.get() in i[0]:
        # Validar el password del usuario
        if password.get() in i[1]:
          # Si todo esta bien el login es validado
          login = True
      
    if(login):
      print("El usuario se encuentra registrado")
    else:
      print("Primero debe registrarse")

  usuarios = lectura_usuarios()
  # Datos de las entradas para nombre y contraseña del usuario en la ventana
  user_name = StringVar()
  password = StringVar()

  frame_form = Frame(ventana, width=700, height=250)
  frame_form.config(bg="white", relief="solid", bd=5)
  frame_form.pack(anchor="center")

  # Labels
  Label(frame_form, text="Nombre usuario: ").pack()
  Entry(frame_form, textvariable=user_name, justify="center").pack()

  Label(frame_form, text="Password usuario: ").pack()
  Entry(frame_form, textvariable=password, justify="center").pack()

  Label(frame_form, text=" ").pack()

  # Buttons
  # ESTE COMMAND LLAMA A LA FUNCIÓN user_reguster() de arriba
  Button(frame_form, text="Registro", command=user_register(usuarios)).pack(
      side="left", fill=X, expand=YES)

  # ESTE COMMAND LLAMA A LA FUNCIÓN log_in() de arriba
  Button(frame_form, text="Login", command=log_in(usuarios)).pack(
      side="left", fill=X, expand=YES)


  ventana.mainloop()