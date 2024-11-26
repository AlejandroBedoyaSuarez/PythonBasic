MondayTemperatures = [9.1 , 8.8 , 8.2]
#los strings de esta lista son KEYS
StudentGrades = {"Alejandro": 9.1, "Edison": 9.2, "David" : 4.2}

mysum= sum (StudentGrades.values())
length= len (StudentGrades.values())
#Promedio
mean= mysum / length
print (mean)