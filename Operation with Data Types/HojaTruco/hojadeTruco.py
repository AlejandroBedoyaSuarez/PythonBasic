"""
                                                                                        Operaciones con Tipos de Datos

Recordemos que:

Las listas, cadenas y tuplas tienen un sistema de índice positivo:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6

Y también tienen un sistema de índices negativos:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4     -3     -2     -1

En una lista, se puede acceder a los elementos 2º, 3º y 4º con

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
Output: ['Tue', 'Wed', 'Thu']

Los tres primeros elementos de una lista:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
Output:['Mon', 'Tue', 'Wed'] 

Los tres últimos elementos de una lista:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
Output: ['Fri', 'Sat', 'Sun']

Todo menos el último:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 

Todo menos los dos últimos:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 

Se puede acceder a un valor de diccionario utilizando su correspondiente clave de diccionario:

phone_numbers = {"Alejandro":"+37682929928","Melody":"+423998200919"}
phone_numbers["Melody"]
Output: '+423998200919'


"""