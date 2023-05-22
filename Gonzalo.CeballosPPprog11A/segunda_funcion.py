#importamos las expresiones regulares
import re

#creamos la funcion con los parametros correspondientes y devolvera un entero
def remplazarCaracteres(cadena:str, caracter, segundo_caracter)->int:
    #el contador tendra la cantidad de veces que se remplazo el caracter
    contador = 0
    #iteramos la cadena y nos fijamos cuantas veces se da la coincidencia
    for caracteres in cadena:
        if(caracteres == segundo_caracter):
            contador += 1
    #hacemos el remplazo
    remplazo = re.sub(caracter, segundo_caracter, cadena)
    print(remplazo)
    #retornamos la cadena
    return contador

print(remplazarCaracteres("holaoaoa", "o", "a"))