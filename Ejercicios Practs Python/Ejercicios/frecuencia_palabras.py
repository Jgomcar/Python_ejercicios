import re

texto = 'Leer este tutorial probablemente reforzó tu interés por usar Python, deberías estar ansioso por aplicar Python a la resolución de tus problemas reales. ¿A dónde deberías ir para aprender más?'

palabras = texto.lower().split()
frecuencias = {}
for palabra in palabras:
    # Pasar palabra a minúsculas, y eliminar todos los caracteres no alfanuméricos
    # \W = [^\w] = 'no letra'; incluye caracteres internacionales, si se usa [^A-Za-z],
    # se eliminan caracteres no ASCII tales como vocales acentuadas, Ñ, Ç ...
    palabra_solo_alfanumerica = re.sub(r'\W+', '', palabra)
    if palabra_solo_alfanumerica in frecuencias:
        frecuencias[palabra_solo_alfanumerica] += 1
    else:
        frecuencias[palabra_solo_alfanumerica] = 1
        
for palabra in sorted(frecuencias):
    print('{}: {}'.format(palabra, frecuencias[palabra]))