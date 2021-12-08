usuarios_clave = open('usuarios.csv','r')
linea = usuarios_clave.readline()

valido = False
while (not valido) and linea:
    if 'Luca'== registro[0] and 'Perro1_-' == registro[1]:
                valido = True
    else:
        linea = usuarios_clave.readline()
        registro = linea.split(',')
usuarios_clave.close()