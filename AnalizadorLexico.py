from Lista import Lista
from Tokens import Token
from ErrorLex import Error

class Analizador:
    def __init__(self) -> None:
        
        self.equivalencias_reservadas = {
            'CrearBD': 'use',
            'EliminarDB': 'DropDataBase',
            'CrarColeccion': 'createCollection',
            'EliminarColeccion': 'dropCollection',
            'InsertarUnico': 'InsertOne'
        }

        self.alfabetoMayusculas = ['A','B','C','D','E','F','G','H','I','J','J','L','M','N','O','P','Q','R','S','T',
                                   'U','V','W','X','Y','Z']
        self.alfabetoMinuscular = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                                   'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.alfabetoNumero = ['0','1','2','3','4','5','6','7','8','9']
        self.ID = ['A','B','C','D','E','F','G','H','I','J','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9']
        self.lista_lexemas = []
        self.string=['\'','\"']

        self.tokens = {
            'RFUNCION': ['CrearBD', 'EliminarBD', 'CrearColeccion', 'EliminarColeccion', 'InsertarUnico', 
                         'ActualizarUnico', 'EliminarUnico', 'BuscarTodo', 'BuscarUnico'],
            'RASIGNACION': '=',
            'RNUEVA': 'nueva',
            'RCOMILLASIMPLES': '\'',
            'RCOMILLASDOBLES':  '\"',
            'RPARENABIERTO': '(',
            'RPARENCERRADO': ')',
            'RPUNTOCOMA': ';',
            'RCOMA': ',',
            'RDOSPUNTOS': ':',
            'RLLAVEABRIR': '{',
            'RLLAVECERRAR': '}'
        }
        
        self.lista_ignorar = ['\n', '\t',' ','-','/','*']
        self.lista = Lista()
        self.lista_errores = Lista()


    def StringJason(self, text):
        json = ''
        count=0
        while True:
            char=text[count]
            if char=='\n':
                self.fila+=1
                self.columna=1
            if (count+1)<len(text):
                char1 = text[count+1]
            if (count+2)<len(text):
                char2 = text[count+2]
            if (count+3)<len(text):
                char3 = text[count+3]
            if char==',':
                count+=1
                json+=str(char)
                continue
            if char =='}':
                if char1 in self.string or char2 in self.string or char3 in self.string:
                    #self.count+=1
                    json+=char
                    return json
            if char =='}':
                if char1 not in self.string or char2 not in self.string:
                    count+=1
                    json+=str(char)
                    continue
            else:
                if char=='\n':
                    self.count+=1
                if char=='\t':
                    self.count+=1
                if char !='\n':
                    #if char!=' ':
                        if char!='\t':
                            json+=str(char)
            count+=1    

    
    def Analizar(self, text):
        
        self.columna = 1
        self.fila =1
        self.count=0
        while self.count<len(text):
            self.char = text[self.count]
            charanterior = text[self.count-1]
            if (self.count+1)<len(text):
                charsiguiente = text[self.count+1]
            
            self.tokensReconocidos(self.char)

            if self.char == '\n':
                self.fila+=1
                self.columna=1

            if self.char=='-' and text[self.count+1]=='-' and text[self.count+2]=='-':
                comentario = self.comentarioLinea(text[self.count:])
                self.count+=len(comentario)-1
                self.columna+=len(comentario)
            if self.char=='-' and text[self.count+1]=='-':
                if text[self.count+2] in self.alfabetoMayusculas or text[self.count+2] in self.alfabetoMinuscular or text[self.count+2] in self.alfabetoNumero:
                    malcomentario = self.comentarioLinea(text[self.count:])
                    self.count+=len(malcomentario)
                    token5 = Error('Léxico',self.fila, self.columna,'Comentario','Falta un simbolo \'-\'')
                    self.lista_errores.insertar(token5)

            if text[self.count] == '/' and text[self.count+1] == '*':
                comentarios = self.comentarioVariasLineas(text[self.count:])
                self.count+=len(comentarios)-1
                self.columna+=len(comentarios)

            if self.char in self.alfabetoNumero:
                if charsiguiente in self.alfabetoMayusculas or charsiguiente in self.alfabetoMinuscular:
                    lexemaError = self.Lexemas(text[self.count:])
                    self.count+=len(lexemaError)-1
                    #self.columna+=len()
                    token0 = Error('Léxico',self.fila, self.columna, 'Error', 'No puede comenzar por numero')
                    self.lista_errores.insertar(token0)

            if self.char not in self.alfabetoMayusculas and self.char not in self.alfabetoMinuscular and self.char not in self.alfabetoNumero and self.char not in self.lista_ignorar:
                aceptacion3 = 0
                for i in self.tokens:
                    if self.char in self.tokens[i] or self.char in self.lista_ignorar:
                        aceptacion3+=1
                if aceptacion3==0:
                    token4 = Error('Léxico',self.fila,self.columna, 'ERROR','Carácter desconocido')
                    self.lista_errores.insertar(token4)
                    aceptacion3=0


            if self.char == '\'' or self.char == '\"':
                aceptacion4=0
                if text[self.count+1]=='{' or text[self.count+2]=='{' or text[self.count+3]=='{':
                    string0 = self.StringJason(text[self.count+1:])
                    self.Strings(string0)

                    self.count+=len(string0)
                    self.char = text[self.count]
                    self.columna+=len(string0)-1
                    aceptacion4=1

                if aceptacion4==0:
                    if self.char == '\'' or self.char == '\"':
                        string = self.Strings2(text[self.count:])
                        if string!=None:
                            self.Strings(string)
                            self.count+=len(string)
                            self.columna+=len(string)-1   
                aceptacion4=0                 
                #continue


            #----------------------------------------FUNCIONES----------------------------------
            if self.char in self.alfabetoMayusculas:
                if charanterior == '\n' or charanterior == ' ':
                    lexema = self.funciones(text[self.count:])
                    self.lista_lexemas.append(lexema)
                    self.count+=len(lexema)-1
                    self.columna+=len(lexema)-1
                    aceptacion = 0
                    for i in self.tokens:
                        if lexema in self.tokens[i]:
                            #print(f'Token: {i} , Lexema: {lexema}, Fila: {self.fila}, Columna: {self.columna}')
                            token = Token(i,lexema,self.fila, self.columna)
                            self.lista.insertar(token)
                            aceptacion=1
                    if aceptacion==0:
                        token1 = Token('RID', lexema, self.fila, self.columna)
                        self.lista.insertar(token1)
                    aceptacion=0
            

            
            if self.char in self.alfabetoMinuscular:
                lexema2 = self.Lexemas(text[self.count:])
                self.lista_lexemas.append(lexema2)
                self.count+=len(lexema2)-1
                aceptacion2=0
                for j in self.tokens:
                    if lexema2 in self.tokens[j]:
                        #print(f'Token: {j} , Lexema: {lexema2}, Fila: {self.fila}, Columna: {self.columna}')
                        token2 = Token(j, lexema2, self.fila, self.columna)
                        self.lista.insertar(token2)
                        aceptacion2=1
                if aceptacion2==0:
                    token3 = Token('RID', lexema2, self.fila, self.columna)
                    self.lista.insertar(token3)
                aceptacion2=0
                self.columna+=len(lexema2)
    
            self.count+=1
            self.columna+=1
        return self.lista


    def Lexemas(self, text):
        count = 0
        lexema = ''
        while count<len(text):
            char = text[count]
            #self.tokensReconocidos(char)
            if char =='\n':
                self.fila+=1
                self.columna=1
            if char == " " or char== '\n' or char =="(" or char=="\"":
                return lexema
            if char in self.alfabetoMayusculas or char in self.alfabetoMinuscular or char in self.alfabetoNumero or char=='=':
                lexema+=char
            else:
                print('error')
            count+=1

    
                

    def comentarioLinea(self, text):
        comentario = ''
        count = 0
        while True:
            char = text[count]
            if char == '\n':
                self.fila+=1
                self.columna=1
                return comentario
            else:
                comentario+=char
            count+=1

    def funciones(self, text):
        funcion = ''
        string = ''
        count = 0
        aceptacion = 0
        while True:
            char = text[count]
            #self.tokensReconocidos(char)
            if char =='\n':
                self.fila+=1
                self.columna=1
            if char == ' ' or char == '\n' or char=='(':
                return funcion
            else:
                funcion+=char
            count+=1

    def comentarioVariasLineas(self, text):
        count = 0
        comentarios = ''
        while True:
            char = text[count]
            if char == '\n':
                self.fila+=1
                self.columna=1
            if char == '*' and text[count+1] == '/':
                return comentarios
            else:
                comentarios+=char
            count+=1

    def errores(self, text):
        token = text
        self.lista_errores.insertar(token)


    def Strings(self, lexema):
        token = Token('STRING',lexema, self.fila, self.columna)
        self.lista.insertar(token)


    def Strings2(self, text):
        string = ''
        count = 0
        aceptacion=0
        while True:
            if count==len(text):
                return None
            if (count+1)<len(text):
                charsiguiente = text[count+1]
            char = text[count]
            if char==')' or char==',':
                return None
            if char == '\'' or char == '\"':
                aceptacion+=1
                if aceptacion==2:
                    return string
            else:
                if char not in self.lista_ignorar and char!=',':
                    string+=char
            count+=1

    '''

    def StringJason(self, text):
        json = ''
        count=0
        while True:
            char=text[count]
            if (count+1)<len(text):
                char2 = text[count+1]
            if char =='}' or char2=='}':
                json+=text[count+1]
                return json
            
            else:
                if char=='\n' and char==' ':
                    self.count+=1
                if char=='\t':
                    self.count+=4
                if char !='\n':
                    if char!=' ':
                        if char!='\t':
                            json+=char
            count+=1    
    '''


            
    def tokensReconocidos(self, lexema):
        for i in self.tokens:
            if lexema == self.tokens[i]:
                self.lista_lexemas.append(lexema)
                token = Token(i,lexema, self.fila, self.columna)
                self.lista.insertar(token)





entrada = '''
--Esto es un comentario de una sola línea
-- Este es otro comentario

/*
Esto es un comentario
de varias
lineas
*/

CrearBD base1 = nueva CrearBD();

EliminarBD eliminarbase1 = nueva EliminarBD('base1');
'''

#j = Analizador()
#j.Analizar(entrada)