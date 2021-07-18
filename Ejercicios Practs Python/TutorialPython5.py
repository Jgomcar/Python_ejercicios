# Metodos de las listas
# list.append(x)
# list.extend(iterable)
# list.insert(i, x)
# list.remove(x)
# list.pop([i])
# list.clear()
# list.index(x[,start[, end]])
# list.count(x)
# list.sort(*,key = None, reverse = False)
# list.reverse()
# list.copy()

#Comprensión de listas
squares = list(map(lambda x: x**2, range(10)))
#equivalentemente a:
squares = [x**2 for x in range(10)]


#Técnicas de iteracción
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
for i, v in enumerate(['tic', 'tac', 'toc']):
    print(i, v)
