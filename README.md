# Readme
Bueno, a partir de ahora el readme queda prolijo para pinchar comentarios pertinentes.

- Función mostrarfichas() Terminada.
- Función turno()  Terminada.
- Función Cambiar() Terminada.
- Creado el archivo pruebas auxiliares así no cambian el main cuando quieren probar su función y lo commitean.
> escuchen, corran la bola...

Creada la función voltear_fichas_para_abajo() para que si las elecciones no son un acierto vuelva la lista a como estaba antes de ese turno.
Incorporado un print que indica si hay un acierto.
Incorporado un print que indica si  termina el juego.
Queda emprolijar los mensajes por pantalla.

boceto de la validación en auxiliares.

Se testeó y aprobó la etapa 2
Se testeó y aprobó la etapa 3
Se testeó y aprobó la etapa 4

Terminadas las etapas 2,3,4. 

Queda por pensar la etapa 5.


## 14/12/2021   COMMIT EN MAIN. CHANGELOG:

### Ahora los usuarios continuan logeados después de una partida, si eligen jugar otra (boton "nueva partida")
- Los usuarios que ya se encuentra logeados aparecen en el listbox.
- El diccionario "dict_jugadores" ahora se encuentra afuera del ciclo de partidas del main (while)
- Al final de cada iteración del ciclo de partidas se resetean las stats de los usuarios logeados.

### Ahora se pueden desloguear usuarios.
- Creado el boton "desloguear Jugador" en la interfaz de login. Desloguea al jugador seleccionado con mouse.
- Los usuarios se pueden logear y desloguear libremente en la interfaz de login siempre que esté abierta.
- Ahora los usuarios no se pueden logear mas de una vez.
- Al desloguear un jugador, se elimina de la listbox y del diccionario de jugadores.
- Los botones de "loguearse" y "Iniciar Partida" se actualizan en relacion al logueo/ deslogueo de jugadores. (según archivo config)

### Ahora se puede salir del juego cerrando la [X] de la ventana de login.
- Al tocar este botón se vacía el diccionario de jugadores y se saltea el resto de las estructuras del main.
- Si se jugó al menos una partida, el ranking de FIN de juego se ejecuta correctamente.

#### Bug fixes: 
- Arreglado bug en que  Iniciar partida estaba desabilitado después de una partida aunque hubiera los usuarios, ya logeados, suficientes.
- Arregladas las stats en partidas sucesivas al cerrar el juego por la interfaz de login.
- Los botones de "iniciar Partida" y "Loguearse" funcionan correctamente según las implementaciones nuevas.
- Los jugadores ya no se pueden loguear mas de una vez.
- Arreglada la posicion del cursor en el archivo csv. EN LA REVISION TENER SIEMPRE ESTO EN CUENTA ANTES DE EJECUTAR.

    
