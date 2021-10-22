
lista_prueba=[["D",False],["D",False],["s",False],["s",False]]
ingreso_in=2

POS_BOOL = 1

def cambiar(fichas,ingreso):
    #Omar Oriz
    #recibe una lista de fichas y un input y devuelve la lista cambiada con la ficha (de pos. ingreso-1) volteada.
    fichas[ingreso-1][POS_BOOL]=True
    return fichas


print(cambiar(lista_prueba,ingreso_in))