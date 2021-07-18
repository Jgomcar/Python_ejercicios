# En Python se pueden usar comillas simples o dobles
s = "Inmersion Python"
t = 'Inmersion Python'
# La ventaja de utilizar comillas dobles es poder utilizar
# las comillas simples en la cadena
if s == t:
    print("iguales")
print(len(s)) #length de el str s = 16
s += ' 3'
print(s)
print(t)

# El docstring de un método proporciona información sobre ese método
# no son obligatorios pero si recomendables si otra persona va a leer
# tu código
def doble_num(numero):
    '''Multiplica el número del parámetro por 2'''
    return numero * 2

# Como ya hemos visto anteriormente, en las cadenas de texto
# se sustituyen las llaves {} por parámetros
usuario = 'mark'
clave = 'System'
# se puede escribir {} o {0}, {1} ...
print("la clave de {0} es {1}".format(usuario,clave))

# ESPECIFICACIONES DE FORMATO
s = '{0:.1f}{1}'.format(698.24, 'GB')
print (s)
# Los dos puntos sirven para marcar el comienzo del especificador de formato
# El especificador 1 significa que redondee a 1
# El especificador 'f' indica que el número se muestre con punto fijo

#cadenas multilínea con las tres comillas '''
s = '''Los archivos son el re-
sultado de años de estudio cientí-
fico...'''
print(s)
# el método splitlines() toma una cadena multilinea y devuelve una lista
# de cadenas de texto, una por cada linea que contuviese la original
print(s.splitlines())
# El método lower() convierte la cadena a minúsculas
# El método upper() lo contrario
# El método count cuenta el nº de veces que aparece un caracter en la cadena
print("")
s = "Mis Invitados Son Excepcionales"
print(s)
print(s.lower())
print (s.upper())
print (s.lower().count('i'))

# Troceado de cadenas
una_cadena = 'Mi vocabulario empieza donde el tuyo termina'
print(una_cadena[3:14])
print(una_cadena[3:-3]) #marcando inicio y fin(con valor negativo que empieza desde el final)
print (una_cadena[0:2]) #devuelve los dos primeros elementos de la cadena: "Mi"
print (una_cadena[:23]) #devuelve la cadena del inicio al elemento 23
print (una_cadena[23:]) #devuelve la cadena del elemento 23 al final
