#Empezamos con las funciones

def promedio (miLista):
            elPromedio= sum(miLista)/ len(miLista)
            return elPromedio

print(promedio([9.1, 4.4, 5.5]))

#Función de conversión de divisas
#Y aquí hay otro ejemplo de una función que convierte una cantidad de dinero de una moneda a otra asumiendo que el tipo de conversión hoy es 1.75.

def convertir(monto):
    resultado = monto * 1.75
    return resultado
print(convertir(10))
#Debe salir 17.5


#Área de un cuadrado (E)
#Defina una función que calcule el área de un cuadrado.

#Por ejemplo, si yo llamara a tu función con foo(7) la salida sería 49. Si la llamara con foo(3) devolvería 9, y así sucesivamente. 
#Ten en cuenta que no tienes que llamar a tu función foo. Dale el nombre que quieras.

def areaCuadrado(area):
        primerLado= 4
        segundoLado= 8
        areaCuadradito= primerLado*segundoLado
        print(areaCuadrado(4)) 

