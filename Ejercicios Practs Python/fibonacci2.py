class Fib:
    '''iterador que genera los números de la secuencia de Fiboinacci'''
   # Método parecido a un constructor
   # 'self' es similar a 'this' en Java, no es una palabra reservada pero si un estándar muy fuerte
   # En __init__ self se refiere al objeto recién creado, en otros métodos se refiere al objeto con el que se llamó
   # 'self' se define explícitamente cuando defines el método pero no cuando lo llamas.
   
   def __init__(self,max):
        self.max = max
        # hay una palabra reservada en Python que significa "sigue adelante, no hay nada que hacer aquí"
        # Sirve para cuando tienes código o métodos a medio hacer
        # Es equivalente a la pareja de llaves vacias de Java {}
        # La palabra es:
        
    
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a +self.b
        return fib
    # Los métodos que tienen __''__ Python los llama cuando utilizas
#     otra sintaxis en la clase o en una instancia de la clase