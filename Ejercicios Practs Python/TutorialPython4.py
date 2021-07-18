# Más herramientas para el control de flujo
# La sentencia if
x = int(input("Introduzca un entero: "))
if x < 0:
    x = 0
    print('negativo\n')
elif x == 0:
    x = 0
    print('cero\n')
else:
    x = 0
    print('mayor\n')
    
# La sentencia for
words = ['cat', 'window', 'door']
for w in words:
    print(w, len(w))
    
# La función range() genera progresiones aritméticas
for i in range(5):
    print (i) #imprime del 0 al 4

#list (range(5,10)) -> [5, 6, 7, 8, 9]
# list (range(0, 10, 3)) -> [0, 3, 6, 9]
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# Decimos que un objeto es iterable si se puede usar en funciones y construcciones que esperan algo
# de lo cual obtener ítems sucesivos hasta que se termine. Hemos visto que la declaración for es una de esas
# construcciones, mientras que un ejemplo de función que toma un iterable es la función sum()
y = sum(range(4)) #0+1+2+3
print(y)

# la sentencia break hace que se salga fuera del bucle sin ejecutar la
# sentencia else (los bucles también tienen else)
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
        
# La sentencia continue:
# La instrucción continue da la opción de omitir
# la parte de un bucle en la que se activa una condición
# externa, pero continuar para completar el resto del
# bucle. Es decir, la iteración actual del bucle se
# interrumpirá, pero el programa volverá a la parte
# superior del bucle.
for num in range(2, 10):
    if num % 2 == 0:
        print ("Found an even number", num)
        continue
    print ("Found an odd number", num)
    
#Definiendo funciones
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()
    

# Fibonacci con retorno
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

# Argumentos con valores por omisión
# Básicamente definir un valor por defecto de los parámetros
def mult(fact1, fact2 = 2):
    return fact1 * fact2
print(mult(4),' ',mult(4, 2),' ',mult(4, 3))
# AVISO: el valor por omisión es evaluado una sola vez
def f(a, L = []):
    L.append(a)
    return L
print(f(1)) #printea [1]
print(f(2)) #printea [1, 2]
print(f(3)) #printea [1, 2, 3]
#Palabras clave como argumentos
def cubo(altura, ancho, color = 'negro', rebota = True):
    print("el cubo de altura {} y anchura {}\n".format(altura, ancho))
    print("tiene un color {}".format(color))
    if rebota:
        print("si que rebota!")
    else: print ("no rebota")
# En esta función, altura y ancho son obligatorios mientras que color y rebota son opcionales
cubo (10, 100)
cubo (10, 100, 'rojo')
cubo (10, 100, 'rojo', False)
cubo (10, 100, rebota = False)
 
# Cuando un parámetro formal de la forma **name está presente al final, recibe un diccionario
# Esto puede ser combinado con un parámetro formal de la forma *name (descrito en la siguiente
# sección) que recibe una tuple conteniendo los argumentos posicionales además de la lista de parámetros formales.
def cheeseshop(kind, *arguments, **keywords):
    print ("-- Do you have any",kind,"?")
    print ("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print (kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, Very runny, sir.",
           shopkeeper = "Michael Palin",
           client = "John Cleese",
           sketch = "Cheese Shop Sketch")

#Diferencias entre parámetros por posición y parámetros por clave
def standard_arg(arg):
    print(arg)
    
#def pos_only_arg(arg, /):
    #print(arg)
def kwd_only_arg(*, arg):
    print(arg)
#def combined_example(pos_only,/, standard, *, kwd_only):
 #   print (pos_only, standard, kwd_only)

standard_arg(2)
standard_arg(arg = 2)

#pos_only(1)
#pos_only(arg = 1) No iría

# kwd_only_arg(3) No iría
kwd_only_arg(arg = 3)

#combined_example(5, 2, kwd_only = 3)

#-----------------------------------------------------------
#Funciones Lambda
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(24)
print(f(5))
    