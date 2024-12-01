#Cortar una lista de 2ª a 4ª (E)
#Imprime la rebanada ['b', 'c', 'd'] de la lista de letras usando rebanar.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#Respuesta
print(letters[1:4])

#Imprime la rebanada ['a', 'b', 'c'] de la lista de letras usando rebanar.
print(letters[:3])

#Imprime la rebanada ['e', 'f', 'g'] de la lista de letras usando rebanar.
print(letters[4:])

#Abra su IDE, cree una variable de datos y asigne un diccionario a esa variable. 

#El diccionario debe contener tres claves, «a», «b» y «c». El valor de la primera clave debe ser [1, 2, 3], el valor de la segunda clave [4, 5, 6], y el valor de la tercera [7, 8, 9].

#¿Cuál sería el resultado de tu código si añadieras print(data['b'][2]) en la segunda línea? Intenta responder sin ejecutar la segunda línea en tu IDE si puedes.

variableDatos= {"a": [1,2,3] , "b": [4,5,6] , "c": [7,8,9] }
print(variableDatos['b'][2])

