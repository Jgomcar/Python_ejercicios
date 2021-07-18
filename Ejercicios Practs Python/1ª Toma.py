print ("Hola a todos!")
var1 = 10
bol = True
while bol:
    var1 = var1 - 1
    print ("procesando...")
    if var1 == 0:
        bol = False
print ("proceso finalizado.")
lista = [1, 2, 3, 'paco', 'pepe']
print (lista)
print ("la longitud de la lista es: " + str(len(lista))) #lista.legth
#para averiguar el índice de un elemento de la lista
print ("el índice de 'paco' es: " + str(lista.index('paco')))
print ("el índice 3 lo ocupa: " + str(lista.count(3)))
#añadir elementos a una lista
lista = lista +  ['joan']
print ("añadimos Joan: " + str(lista))
lista.append(13)
lista.extend([18, 19])
print ("añadimos nº" + str(lista))
#hay distintas formas de borrar un elemento de una lista
#si te sabes el índice:
del lista[3]
print("hemos borrado a paco " + str(lista))
#si no sabemos el índice:
lista.remove('pepe')
print("hemos borrado a pepe " + str(lista))
#también se puede extraer
print("lista.pop(): " + str(lista.pop()))
print (lista)
print ("lista.pop(1): " + str(lista.pop(1)))
#lista vacia = False, lista con al menos 1 elemento = True
def es_true(anything):
    if anything:
        print("sí, es true")
    else:
        print("no, es false")
        
es_true(lista)
es_true([])
#Concatenar variables con strings para escribir
numInvitados = 20
numCopas = 18
print("Somos {} invitados y hay {} copas".format(numInvitados, numCopas))
# Tuplas: inmutables, una vez creada no se puede añadir ni borrar
v = ('a' , 2, True)
(x,y,z) = v
print(x) #escribe 'a'
print(y) #escribe 2
#La función range genera una secuencia de números enteros
(LUNES, MARTES, MIERCOLES, JUEVES, VIERNES, SABADO, DOMINGO) = range(7)
print (LUNES) #escribe 0
print (MARTES) #escribe 1
#Nota del tutor:
#Ya que estamos, un detalle sobre nombres de variables (y funciones): en Python se acostumbra a usar identificadores en minúsculas separados por _
#Es decir, num_invitados en lugar de numInvitados
#Los nombres de clases (cuando llegues a eso) en cambio suelen nombrarse con IdentificadoresComoEste
#No es obligatorio, pero hay definidos unos estándares que conviene seguir; así te acostumbras y luego resulta más fácil leer código escrito por otros

#Un conjunto es una ``bolsa'' sin ordenar de valores únicos.
un_conjunto = 1, 2
print (un_conjunto)
#se pueden crear a partir de una lista.
una_lista = ['a', 'b', 'jgomcar', True]
un_conjunto = set(una_lista)
print(un_conjunto)
#crear un conjunto vacío
un_conjunto = set()
print("longitud de un_conjunto: {}".format(len(un_conjunto)))
#para añadir elementos en conjuntos: 2 maneras
#1ª método add, le pasas un elemento
un_conjunto.add(4)
print (un_conjunto)
#2ª método update, le pasas varios elementos
#en los conjuntos no pueden haber elementos repetidos
una_lista = [1, 2, 3]
un_conjunto = set(una_lista)
un_conjunto.update([2, 4, 6])
print(un_conjunto)
#Operaciones básicas con conjuntos
un_conjunto = {1, 3, 6, 10, 15, 21, 28, 36, 45}
un_conjunto.discard(10)#elimina el elemento 10
print(un_conjunto)
print(un_conjunto.pop())
print(un_conjunto)
#limpiar un conjunto
# un_conjunto.clear() elimina todos los elementos
# comprobar si un elemento está en el conjunto
print(str(30 in un_conjunto)) #False porque no está
#conjunto simétrico. unión, intersección, y diferencia
otro_conjunto = set()
otro_conjunto = otro_conjunto.symmetric_difference(un_conjunto)
print(otro_conjunto)
otro_conjunto.union(un_conjunto)
otro_conjunto.intersection(un_conjunto)
otro_conjunto.difference(un_conjunto)

#Diccionarios: conjunto de parejas clave-valor
un_dic = {'servidor': 'db.server.org', 'basedatos': 'mysql'}
print(un_dic)
print(un_dic['servidor'])
#Modificación de un diccionario
un_dic['servidor'] = 'servidor.es' #modifica un valor con la clave
print(un_dic['servidor'])
un_dic['usuario'] = 'usulocal' #añade nueva entrada con nueva clave
print(un_dic)
#Diccionarios con valores mixtos
SUFIJOS = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
           1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
print(SUFIJOS[1000][3])
#Constante especial None de Python
#no se pueden crear más constantes de tipo NoneType
# sin embargo se puede asignar a una variable
x = None
print(str(x == None))