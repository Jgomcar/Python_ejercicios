import re
import sys

#texto = 'Leer este tutorial probablemente reforzó tu interés por usar Python, deberías estar ansioso por aplicar Python a la resolución de tus problemas reales. ¿A dónde deberías ir para aprender más?'

def frecuencia_palabras(texto):
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
    return frecuencias

if __name__ == '__main__':
    # Obtener el nombre del archivo del primer parámetro de la línea de comandos
    # (el parámetro 0 es siempre el nombre del módulo Python)
    if len(sys.argv) < 2:
        # En lugar de usar "print", que envía la salida a "stdout", enviamos el mensaje a "stderr":
        sys.stderr.write('Error: falta el nombre del archivo con el texto a procesar\n')
        exit(1)
    nombre_archivo = sys.argv[1]
    # Abrir el archivo y leer el contenido
    try:
        # Si no se indica el "encoding", se usa la codificación por defecto del sistema;
        # en Windows suele ser "cp1252". Asumimos que el texto está codificado en UTF-8:
        archivo = open(nombre_archivo, 'r', encoding='utf-8')
        texto = archivo.read()
        frecuencias = frecuencia_palabras(texto)
        for palabra in sorted(frecuencias):
            print('{}: {}'.format(palabra, frecuencias[palabra]))
    except FileNotFoundError:
        sys.stderr.write('Error: no se encuentra el archivo de entrada\n')
    except Exception as e:
        sys.stderr.write('Error: {}\n'.format(e))
    finally:
        archivo.close()    
