from AnalizadorLexico import Analizador
from ErrorLex import Error

class Sintactico:
    def __init__(self) -> None:
        self.lista = []
        comillas = ['\'','\"']
        self.CrearBD = ['CrearBD','RID','=' ,'nueva', 'CrearBD','(',')',';']
        self.EliminarBD = ['EliminarBD','RID','=','nueva','EliminarBD','(',comillas,'STRING',comillas,')',';']
        self.CrearColec = ['CrearColeccion','RID','=','nueva','CrearColeccion','(',comillas,'STRING',comillas,')',';']
        self.EliminarColec = ['EliminarColeccion','RID','=','nueva','EliminarColeccion','(',comillas,'STRING',comillas,')',';']
        self.BuscarT = ['BuscarTodo','RID','=','nueva','BuscarTodo','(',comillas,'STRING',comillas,')',';']
        self.BuscarU = ['BuscarUnico','RID','=','nueva','BuscarUnico','(',comillas,'STRING',comillas,')',';']
        self.InsertarU = ['InsertarUnico','RID','=','nueva','InsertarUnico','(',comillas,'STRING',comillas,',',comillas,'STRING',comillas,')',';']
        self.EliminarU = ['EliminarUnico','RID','=','nueva','EliminarUnico','(',comillas,'STRING',comillas,',',comillas,'STRING',comillas,')',';']
        self.ActualizarU = ['ActualizarUnico','RID','=','nueva','ActualizarUnico','(',comillas,'STRING',comillas,',',comillas,'STRING',comillas,')',';'] 
        self.doc = ''

    def compila(self, documento):
        self.compilar = Analizador()
        self.compilar.Analizar(documento)
        self.Sintactico()


    def Sintactico(self):
        i = 0
        while i<self.compilar.lista.tamaño:
            char = self.compilar.lista.indexar(i)
            charsiguiente = self.compilar.lista.indexar(i+1)
            lexema = char.Lexema

            if lexema =='CrearBD' and char.Token=='RFUNCION' and charsiguiente.Lexema!='(':
                self.Crear(i)
            if lexema=='EliminarBD' and char.Token=='RFUNCION' and charsiguiente.Lexema!='(':
                self.Eliminar(i)
            if lexema=='CrearColeccion' and char.Token=='RFUNCION' and charsiguiente.Lexema!='(':
                self.CrarCole(i)
            if lexema=='EliminarColeccion' and char.Token=='RFUNCION' and charsiguiente.Lexema!='(':
                self.EliminarCole(i)
            if lexema=='BuscarTodo' and char.Token=='RFUNCION' and charsiguiente.Lexema!='(':
                self.BuscarTodo(i)
            if lexema=='BuscarUnico' and char.Token=='RFUNCION' and charsiguiente.Lexema!='(':
                    self.BuscarUnico(i)
            if lexema=='InsertarUnico' and char.Token=='RFUNCION' and charsiguiente.Lexema!='(':
                self.InsertarUnico(i)
            if lexema=='EliminarUnico' and char.Token =='RFUNCION' and charsiguiente.Lexema!='(':
                self.EliminarUnico(i)
            if lexema=='ActualizarUnico' and char.Token=='RFUNCION' and charsiguiente.Lexema!='(':
                self.ActualizarUnico(i)

            i+=1
        self.crearArchivo()

    def Crear(self, i):
        k = i
        aceptar = 0
        for i in self.CrearBD:

            if self.compilar.lista.indexar(k).Lexema == i or self.compilar.lista.indexar(k).Token==i:
                if self.compilar.lista.indexar(k).Token=='RID':
                    id = self.compilar.lista.indexar(k).Lexema
                
                aceptar+=1
            if aceptar==len(self.CrearBD):
                crear = f'\nuse(\'{id}\');\n'
                self.doc+=crear
                break
            k+=1
                
    def Eliminar(self,i):
        k = i
        aceptar = 0
        for i in self.EliminarBD:
            char =self.compilar.lista.indexar(k).Lexema 
            if self.compilar.lista.indexar(k).Lexema == i or self.compilar.lista.indexar(k).Token==i or self.compilar.lista.indexar(k).Lexema in i:
                if self.compilar.lista.indexar(k).Token=='STRING':
                    id = self.compilar.lista.indexar(k).Lexema
                
                aceptar+=1
            if aceptar==len(self.EliminarBD):
                crear = f'\ndb.dropDatabase(\'{id}\');\n'
                self.doc+=crear
                break
            k+=1

    def CrarCole(self, i):
        k = i
        aceptar = 0
        for i in self.CrearColec:

            if self.compilar.lista.indexar(k).Lexema == i or self.compilar.lista.indexar(k).Token==i or self.compilar.lista.indexar(k).Lexema in i:
                if self.compilar.lista.indexar(k).Token=='STRING':
                    id = self.compilar.lista.indexar(k).Lexema
                
                aceptar+=1
            if aceptar==len(self.CrearColec):
                crear = f'\ndb.createCollection(\'{id}\');\n'
                self.doc+=crear
                break
            k+=1


    def EliminarCole(self,i):
        k = i
        aceptar = 0
        for i in self.EliminarColec:

            if self.compilar.lista.indexar(k).Lexema == i or self.compilar.lista.indexar(k).Token==i or self.compilar.lista.indexar(k).Lexema in i:
                if self.compilar.lista.indexar(k).Token=='STRING':
                    id = self.compilar.lista.indexar(k).Lexema
                
                aceptar+=1
            if aceptar==len(self.EliminarColec):
                crear = f'\ndb.{id}.drop();\n'
                self.doc+=crear
                break
            k+=1  

    def BuscarTodo(self,i):
        k = i
        aceptar = 0
        for i in self.BuscarT:

            if self.compilar.lista.indexar(k).Lexema == i or self.compilar.lista.indexar(k).Token==i or self.compilar.lista.indexar(k).Lexema in i:
                if self.compilar.lista.indexar(k).Token=='STRING':
                    id = self.compilar.lista.indexar(k).Lexema
                
                aceptar+=1
            if aceptar==len(self.BuscarT):
                crear = f'\ndb.{id}.find();\n'
                self.doc+=crear
                break
            k+=1  

    def BuscarUnico(self,i):
        k = i
        aceptar = 0
        for i in self.BuscarU:
            char = self.compilar.lista.indexar(k).Lexema
            if self.compilar.lista.indexar(k).Lexema == i or self.compilar.lista.indexar(k).Token==i or self.compilar.lista.indexar(k).Lexema in i:
                if self.compilar.lista.indexar(k).Token=='STRING':
                    id = self.compilar.lista.indexar(k).Lexema
                
                aceptar+=1
            if aceptar==len(self.BuscarU):
                crear = f'\ndb.{id}.findOne();\n'
                self.doc+=crear
                break
            k+=1  

    def InsertarUnico(self,i):
        k = i
        string1 =0
        aceptar = 0
        for i in self.InsertarU:
            char = self.compilar.lista.indexar(k).Lexema
            if self.compilar.lista.indexar(k).Lexema == i or self.compilar.lista.indexar(k).Token==i or self.compilar.lista.indexar(k).Lexema in i:
                if self.compilar.lista.indexar(k).Token=='STRING' and string1==1:
                    json = self.compilar.lista.indexar(k).Lexema
                if self.compilar.lista.indexar(k).Token=='STRING' and string1==0:
                    id = self.compilar.lista.indexar(k).Lexema
                    string1+=1
                aceptar+=1
            if aceptar==len(self.InsertarU):
                crear = f'\ndb.{id}.insertOne(\"{json}\");\n'
                self.doc+=crear
                break
            k+=1  
              

    def EliminarUnico(self,i):
        k = i
        string1 =0
        aceptar = 0
        for i in self.EliminarU:
            char = self.compilar.lista.indexar(k).Lexema
            if self.compilar.lista.indexar(k).Lexema == i or self.compilar.lista.indexar(k).Token==i or self.compilar.lista.indexar(k).Lexema in i:
                if self.compilar.lista.indexar(k).Token=='STRING' and string1==1:
                    json = self.compilar.lista.indexar(k).Lexema
                if self.compilar.lista.indexar(k).Token=='STRING' and string1==0:
                    id = self.compilar.lista.indexar(k).Lexema
                    string1+=1
                aceptar+=1
            if aceptar==len(self.EliminarU):
                crear = f'\ndb.{id}.deleteOne(\"{json}\");\n'
                self.doc+=crear
                break
            k+=1  

    def ActualizarUnico(self,i):
        k = i
        string1 =0
        aceptar = 0
        for i in self.ActualizarU:
            char = self.compilar.lista.indexar(k).Lexema
            if self.compilar.lista.indexar(k).Lexema == i or self.compilar.lista.indexar(k).Token==i or self.compilar.lista.indexar(k).Lexema in i:
                if self.compilar.lista.indexar(k).Token=='STRING' and string1==1:
                    json = self.compilar.lista.indexar(k).Lexema
                if self.compilar.lista.indexar(k).Token=='STRING' and string1==0:
                    id = self.compilar.lista.indexar(k).Lexema
                    string1+=1
                aceptar+=1
            if aceptar==len(self.ActualizarU):
                crear = f'\ndb.{id}.updateOne(\"{json}\");\n'
                self.doc+=crear
                break
            k+=1
        if aceptar!=len(self.ActualizarU):
            error = Error('Sintáctico',self.compilar.lista.indexar(k).fila , self.compilar.lista.indexar(k).columna,self.compilar.lista.indexar(k).Token,'Errore de orden o hace falta altun dato o carater')
            self.compilar.lista_errores.insertar(error)


    def crearArchivo(self):
        arch = open('Salida.txt','w')
        arch.write(self.doc)
        arch.close()