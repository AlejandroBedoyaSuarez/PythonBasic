#Hoja de trucos: Tipos de datos

#En esta sección has aprendido que:

#Los números enteros se usan para representar números enteros:
rango = 10
huevos = 12
personas = 3

#Los flotantes representan números decimales
temperatura = 10.2
precipitación = 5.98
altitud = 1031.88

#Las cadenas representan texto:
mensaje = "¡Bienvenido a nuestra tienda online!"
nombre = "Juan"
serie = "R001991981SW"

#Las listas representan matrices/arrays de valores que pueden cambiar durante el transcurso del programa:
members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]

#Los diccionarios representan pares de claves y valores:
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}

#Las claves de un diccionario pueden extraerse con
phone_numbers.keys()

#Los valores de un diccionario se pueden extraer con:
phone_numbers.values()

#Las tuplas representan matrices de valores que no deben modificarse durante el transcurso del programa:
vocales = ('a', 'e', 'i', 'o', 'u')
un_dígito = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

#Puede obtener una lista de atributos de un tipo de datos tiene utilizando:
dir(str)
dir(list)
dir(dict)

#Puedes obtener una lista de las funciones incorporadas de Python utilizando:
dir(__builtins__)

#Puedes obtener la documentación de un tipo de dato Python usando:
help(str)
help(str.replace)
help(dict.values)