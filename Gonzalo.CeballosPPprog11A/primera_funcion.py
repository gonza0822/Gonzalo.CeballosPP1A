#creo la funcion con un parametro que debe ser un entero(precio) y la funcion devolvera un int 
def aplicarAumento(precio:int)->int:
    #aumento guarda el porcentaje de aumento
    aumento = 5
    #el precio final se obtiene de que a precio se le sume el precio multiplicado por el aumento dividido 100(el porcentaje en pesos)
    precio_final = precio + (precio * (aumento/100))
    #por ultimo retornamos el precio con el aumento
    return precio_final

print(aplicarAumento(100))