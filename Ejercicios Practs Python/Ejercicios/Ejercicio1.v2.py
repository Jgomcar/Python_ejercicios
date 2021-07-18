import re
import sys
import io

# Se trata de escribir un programa que a partir de una cadena de texto, como este ejemplo:

# texto = 'Leer este tutorial probablemente reforzó tu interés por usar Python, deberías estar
# ansioso por aplicar Python a la resolución de tus problemas reales. ¿A dónde deberías ir para aprender más?'

# Modifícalo para que lea el nombre de un archivo desde la línea de comandos,
# lea desde el archivo el texto a procesar, y lo demás igual.
   
def veces_aparicion_archivo(archivo):
    # Utilizando with no necesitaría open() y close()
    # sería->
    with io.open(archivo, 'r', encoding = 'utf-8') as archivo:
#         archivo = io.open(archivo, 'r', encoding = 'utf-8')
        repeticiones = {}
    # Recorrer cada linea del archivo
        for linea in archivo:
            palabras = linea.lower().split()
        # Recorrer cada palabra de cada linea del archivo
            for palabra in palabras:
                palabra_solo_alfanumérica = re.sub(r'[^\w]+',"",palabra)
            
                if palabra_solo_alfanumérica in repeticiones:
                    repeticiones[palabra_solo_alfanumérica] += 1
                else:
                    repeticiones[palabra_solo_alfanumérica] = 1
    
    # Ordenar e imprimir por pantalla con formato
        for palabra in sorted(repeticiones):
            print(f'{palabra:10} ==> {repeticiones[palabra]:2d}')    
#         archivo.close()
    
    
# def prueba(nombre_archivo):
#     archivo = open(nombre_archivo, 'r')
#     for linea in archivo:
#         print (linea)
#     archivo.close()

try:
    nombre_archivo = (sys.argv[1])
    veces_aparicion_archivo(nombre_archivo)
except FileNotFoundError:
    print("Archivo no encontrado")
    print("introduzca 'nombre_archivo.extensión'")
except IndexError:
    print("Especifique el nombre del archivo")
except:
    print("Error desconocido:", sys.exc_info()[0])

# prueba(sys.argv[1])