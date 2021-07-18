#Listas por compresión
#  Para explicar esto es mejor leerlo de derecha a
#  izquierda. una_lista es la lista origen que se va
#  a recorrer para generar la nueva lista.
#  El intérprete de Python recorre cada uno de los
#  elementos de una_lista, asignando temporalmente
#  el valor de cada elemento a la variable elem.
#  Después Python aplica la operación que se haya
#  indicado, en este caso elem * 2, y el resultado
#  lo añade a la nueva lista
una_lista = [1, 9, 8, 4]
lista_mod = [elem * 2 for elem in una_lista]
print(lista_mod)

# Truco para intercambiar claves y valores en un diccionario.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {value: key for key, value in dict1.items()}
print(dict1)
print(dict2)
# Conjuntos por comprensión
conjunto = set(range(10))
print(conjunto)
conjunto_1 = [x ** 2 for x in conjunto]
conjunto_2 = [x for x in conjunto if x]
conjunto_3 = [2 ** x for x in range(10)]
print(conjunto_1)
print(conjunto_2)
print(conjunto_3)