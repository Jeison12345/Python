# Algunas variables
cadena_texto = "Hola Python"
print(cadena_texto)

numero = 5
print(numero)

booleana = True
print(booleana)

#print puede recibir mas de un elemento, asi:
print(cadena_texto, numero, booleana)
print("Tengo el numero:", numero)

#Tambien podemos cambiar el tipo de dato, asi:
numero_a_cadena = str(numero) #Pasamos la varible que queremos convertir
print(type(numero_a_cadena))

#Ya que Python tiene un tipado dinamico, tambien se puede cambiar el tipo asi:
numero = "Jeison" #aunque numero era de tipo int, ahora la he cambiado a tipo str

#podemos saber la longitud con la siguiente funcion del sistema
print(len(cadena_texto))

#Tambien podemos declarar variables en una sola linea (No abusar de esto)
nombre, apellido, edad = "Jeison", "Rico", 21
