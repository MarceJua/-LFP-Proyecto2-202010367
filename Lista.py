#from Tokens import Token
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.primero = None
        self.tamaño = 0

    def insertar(self,dato):
        nuevo = Nodo(dato)
        if self.primero == None or self.tamaño == 0:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamaño+=1

    def imprimir(self):
        actual = self.primero
        while actual!=None:
            print(actual.dato)
            actual = actual.siguiente

    def indexar(self, index):
        contador=0
        actual = self.primero
        while actual!= None:
            if contador == index:
                return actual.dato
            contador+=1
            actual= actual.siguiente


'''
j = Lista()
nodo1 = Token('dd','rr',4,5)
nodo2 = Token('ff','tt',5,6)
nodo3 = Token('gg','yy',6,7)
nodo4 = Token('hh','uu',7,8)
nodo5 = Token('jj','ii',8,9)
j.insertar(nodo1)
j.insertar(nodo2)
j.insertar(nodo3)
j.insertar(nodo4)
nodo = j.indexar(2)
print(nodo.Lexema)
'''