#Operadores aritmeticos
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 2) #modulo o residuo
print(10 // 3) #division aproximada a un entero
print(2 ** 8) #potencia

#El operador + puede utilizarse tambien para concatenar, asi:
print("Hola" + "Python")

"""
No podriamos concatenar un str con un entero asi:
print("Hola" + 3)
pero si podemos utilizar otro operador para que dos tipos de datos interactuen
como por ejeplo el operador *
"""

print("Hola" * 3) #En este caso la cadena "Hola" se imprimira tres veces

#Operadores comparativos
print(3 < 4)
print(3 > 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)

#Tambien con cadenas de texto
print("aaaa" >= "abaa") #El resultado de esta comparacion es definido por la ordenacion alfabetica por ASCII
print(len("aaaa") >= len("abaa")) #El resultado de esta comparacion es definido por el numero de caracteres

#Operadores logicos (Estudiar logica para entender mejor este tema)
print(5 > 3 and "aaaa" >= "abaa")
print(5 > 3 or "aaaa" >= "abaa")
print(not(3 > 5))