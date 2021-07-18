import re
from collections import OrderedDict

# def prueba (frase):
#     word = ''
#     frase += ' '
#     for x in frase:
#         if x == ' ':
#             print (word, '\n')
#             word = ''
#         else:
#             word += x
            
#prueba('esto es una prueba')

# Se trata de escribir un programa que a partir de una cadena de texto, como este ejemplo:

# texto = 'Leer este tutorial probablemente reforzó tu interés por usar Python, deberías estar
# ansioso por aplicar Python a la resolución de tus problemas reales. ¿A dónde deberías ir para aprender más?'

# liste por pantalla la frecuencia de aparición de cada palabra, es decir, de como salida
# cada palabra que aparece en el texto, y el número de veces que aparece

def veces_aparicion3(frase):
    palabras = frase.lower().split()
    palabras = sorted(palabras)
    repeticiones = OrderedDict()
    for palabra in palabras:
        palabra_solo_alfanumérica = re.sub(r'[^\w]+',"",palabra)
        if palabra_solo_alfanumérica in repeticiones:
            repeticiones[palabra_solo_alfanumérica] += 1
        else:
            repeticiones[palabra_solo_alfanumérica] = 1
    print(repeticiones)

veces_aparicion3('Leer este tutorial probablemente reforzó tu interés por usar Python, deberías estar ansioso por aplicar Python a la resolución de tus problemas reales. ¿A dónde deberías ir para aprender más?')

def veces_aparicion2(frase):
    palabras = frase.lower().split()
    palabras = sorted(palabras)
    repeticiones = OrderedDict()
#     encontrado = False
    for palabra in palabras:
        palabra_solo_alfanumérica = re.sub(r'[^\w]+',"",palabra)
#         for palabras_diccionario, numero_repeticiones in repeticiones.items():
#             if palabra_solo_alfanumérica == palabras_diccionario:
#                 encontrado = True
#                 numero_repeticiones = numero_repeticiones + 1
#                 repeticiones[palabra_solo_alfanumérica] = numero_repeticiones
#                 break
#         if not encontrado:
#             repeticiones[palabra_solo_alfanumérica] = 1
#         else:
#             pass
        if palabra_solo_alfanumérica in repeticiones:
            numero_repeticiones = repeticiones[palabra_solo_alfanumérica]
            numero_repeticiones = numero_repeticiones + 1
            repeticiones[palabra_solo_alfanumérica] = numero_repeticiones
        else:
            repeticiones[palabra_solo_alfanumérica] = 1
#         encontrado = False 
    print(repeticiones)
    
#veces_aparicion2('Leer este tutorial probablemente reforzó tu interés por usar Python, deberías estar ansioso por aplicar Python a la resolución de tus problemas reales. ¿A dónde deberías ir para aprender más?')

# def veces_aparicion(frase):
#     frase += ' '
#     re.sub(r'[^\w]+',"",)
#     word = ''
#     rep = {}
#     encontrado = False
#     for x in frase:
#         x = x.lower()
#         if x == ' ':
#             for w, n in rep.items():
#                 if word == w:
#                     encontrado = True
#                     n = n + 1
#                     rep[word] = n
#                     break
#             if not encontrado:
#             rep[word] = 1
#             encontrado = False
#             word = ''
#         elif sin_tilde(x) >= 'a' and sin_tilde(x) <= 'z':
#             word += x
#         #elif x >= chr(128) and x <= chr(165):
#             #word += x
#         else:
#             pass
#     print(rep)
# 
# def sin_tilde(s):
#     vocales = (("á","a"), ("é","e"),("í","i"),("ó","o"),("ú","u"))
#     for a, b in vocales:
#         s = s.replace(a,b)
#     return s

