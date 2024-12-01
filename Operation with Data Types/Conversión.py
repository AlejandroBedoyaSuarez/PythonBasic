"""
Consejo: Conversión entre tipos de datos
A veces puede que necesites convertir entre diferentes tipos de datos en Python por una razón u otra. Esto es muy fácil de hacer:

De tupla a lista:

>>> cool_tupla = (1, 2, 3)
>>> cool_list = list(cool_tupla)
>>> cool_list
[1, 2, 3]


De lista a tupla:

>>> cool_list = [1, 2, 3]
>>> cool_tuple = tuple(cool_list)
>>> tupla_frío
(1, 2, 3)

De string to list:

>>> cool_string = "Hello"
>>> cool_list = list(cool_string)
>>> cool_list
['H', 'e', 'l', 'l', 'o']#

De list to string:

>>> cool_list = ['H', 'e', 'l', 'l', 'o']
>>> cool_string = str.join("", cool_list)
>>> cool_string
'Hello'

Como se puede ver más arriba, convertir una lista en una cadena es más complejo. Aquí str() no es suficiente.
Necesitamos str.join(). 
Prueba a ejecutar de nuevo el código anterior, pero esta vez utilizando str.join(«---», cool_list) en la segunda línea.
Entenderás cómo funciona str.join().
"""


