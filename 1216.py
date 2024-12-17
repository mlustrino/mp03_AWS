lista = [100,15,89,68,75,27,3]
# lista = [100,89,75,27,3]
def doPasada(lista):
    resultado =[]
    if len(lista) ==1:
        resultado = lista
        return resultado
    if lista[0] > lista[1]:
        aux = lista[0]
        lista[0] = lista[1]
        lista[1] = aux
    resultado.append(lista[0])
    resultado = resultado + doPasada(lista[1:])
    return resultado

def doBubble(lista):
    resultado = []
    if len(lista) == 1:
        return lista
    listaDespuesPasada = doPasada(lista)
    resultado.append(listaDespuesPasada[-1])
    resultado = doBubble(listaDespuesPasada[:len(listaDespuesPasada) - 1]) + resultado
    return resultado


#print(doPasada(lista))
print(doBubble(lista))
#
#
# def doPasadaOrd(lista, ordre):
#     resultado =[]
#     if len(lista) ==1:
#         resultado = lista
#         return resultado
#     if ordre == "asc" and lista[0] > lista[1]:
#         aux = lista[0]
#         lista[0] = lista[1]
#         lista[1] = aux
#     elif ordre == "desc" and lista[0] < lista[1]:
#         aux = lista[1]
#         lista[1] = lista[0]
#         lista[0] = aux
#     resultado.append(lista[0])
#     resultado = resultado + doPasadaOrd(lista[1:], ordre)
#     return resultado
#


#print(doPasadaOrd(lista, "asc"))

#print(doPasadaOrd(lista, "desc"))