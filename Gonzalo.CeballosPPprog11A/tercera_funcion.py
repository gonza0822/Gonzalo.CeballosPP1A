def ordenarCaracteres(cadena:str)->str:
    for i in range(len(cadena) - 1):
        for j in range(i +1, len(cadena)):
            if cadena[i] > cadena[j]:
                aux = cadena[i]
                cadena[i] = cadena[j]
                cadena[j] = aux
    return cadena

print(ordenarCaracteres("hola"))
