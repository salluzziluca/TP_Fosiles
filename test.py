from Constantes import MAX_JUGADORES


dict_jugadores = {1:1, 2:2, 3:3, 4:4}
MAX_JUGADORES = 4
usuario = 'Luca'
contraseña = 'ssss'
def presionar_enviar():
        # Valentina Nieto,Oriz Omar, Luca Salluzzi,Agustín Conti,Lucas Osorio.
        #No recibe nada. se ejecuta al presionar el Boton. Asigna el contenido de los entry al diccionario de jugadores. Cierra la interfaz.
        if len(dict_jugadores.keys())< MAX_JUGADORES:
            if True:
                dict_jugadores[usuario] = [0,0]
                print('si')
            else:
                print('no)')
                
        else:
            print('ajugar')
        return None
presionar_enviar()