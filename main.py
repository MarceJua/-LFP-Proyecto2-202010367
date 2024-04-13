from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfile
import tkinter.messagebox
from ttkthemes import ThemedStyle

class Interfaz:
    def __init__(self):
        self.pantalla_principal = Tk()
        self.pantalla_principal.geometry('1300x650')
        self.pantalla_principal.config(bg='#f0f0f0')  #color de fondo
        style = ThemedStyle(self.pantalla_principal)
        style.set_theme("arc")  # tema de estilo "arc"
        self.componenentes()
        self.menu()
        
        self.pantalla_principal.mainloop()

    def componenentes(self):
        # Texto derecho
        self.texto_derecho = Text(self.pantalla_principal)
        self.texto_derecho.config(height=20, width=48, bg='#ffffff', border=0, fg='#000000', 
                                  insertbackground='black', font=('Helvetica',12), padx=11)
        self.texto_derecho.place(x=725,y=120)
        
        # Texto izquierdo
        self.texto_izquierdo = Text(self.pantalla_principal)
        self.texto_izquierdo.config(height=20, width=45, bg='#ffffff', border=0, fg='#000000',
                               insertbackground='black', font=('Helvetica', 12), padx=11, wrap='word')
        self.texto_izquierdo.place(x=50,y=120)           
        
        # Botón Analizar
        Analizar = Button(self.pantalla_principal, text='Analizar', font=('Helvetica', 12), command=self.analizar)
        Analizar.place(x=575, y=250)
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////
    def menu(self):
        self.menu1 = Menu(self.pantalla_principal)
        self.menu1.config(bg='#f0f0f0')
        #--------------------------------------------
        self.filemenu = Menu(self.menu1, tearoff=0)
        self.filemenu.add_command(label='Nuevo')
        self.filemenu.add_command(label='Abrir', command=self.Abrir)
        self.filemenu.add_command(label='Guardar', command=self.Guardar)
        self.filemenu.add_command(label='Guardar Como')
        self.filemenu.add_command(label='Salir', command=self.Salir)
        #--------------------------------------------

        opcion1 = self.menu1.add_cascade(label='Archivo', menu=self.filemenu)
        #opcion2 = self.menu1.add_cascade(label='Análisis')
        opcion3 = self.menu1.add_command(label='Tokens', command=self.TablaTokens)
        opcion4 = self.menu1.add_command(label='Errores', command=self.TablaErrores)
        
        self.pantalla_principal.config(menu=self.menu1)
        
    def TablaTokens(self):
        pantalla_tokens = Tk()
        pantalla_tokens.geometry('750x550')
        pantalla_tokens.config(bg='#f0f0f0')
        tabla = ttk.Treeview(pantalla_tokens, columns=('col1','col2'))
        tabla.column('#0',width=80, anchor='center')
        tabla.column('#1',width=170, anchor='center')
        tabla.column('#2',width=270, anchor='center')
        tabla.heading('#0', text='Número', anchor='center')
        tabla.heading('#1', text='Token', anchor='center')
        tabla.heading('#2', text='Lexema', anchor='center')
        scrollbar = ttk.Scrollbar(pantalla_tokens,orient=VERTICAL, command=tabla.yview)
        tabla.config(yscrollcommand=scrollbar.set, height=30)
        scrollbar.place(x=635, y=30, height=490)
        #tabla.config(height=20)
        tabla.pack(padx=20, pady=30)

        actual = self.compilar.compilar.lista.primero
        count = 0
        while actual!=None:
            count+=1
            tabla.insert('',END,text=count, values=(actual.dato.Token,actual.dato.Lexema))
            print(actual.dato.Token+ '     >    ' +actual.dato.Lexema)
            actual = actual.siguiente

    def TablaErrores(self):
        error = Tk()
        error.geometry('850x450')
        error.config(bg='#f0f0f0')
        tabla = ttk.Treeview(error, columns=('col1','col2','col3','col4'))
        tabla.column('#0', width=150, anchor='center')
        tabla.column('#1', width=80, anchor='center')
        tabla.column('#2', width=80, anchor='center')
        tabla.column('#3', width=150, anchor='center')
        tabla.column('#4', width=300, anchor='center')
        tabla.heading('#0', text='Tipo', anchor='center')
        tabla.heading('#1', text='Linea', anchor='center')
        tabla.heading('#2', text='Columna', anchor='center')
        tabla.heading('#3', text='Esperado', anchor='center')
        tabla.heading('#4', text='Descripcion', anchor='center')
        tabla.config(height=20)
        tabla.pack(padx=20,pady=20)
        
        actual = self.compilar.compilar.lista_errores.primero
        while actual!= None:
            tabla.insert('',END,text=actual.dato.tipo, values=(actual.dato.linea, actual.dato.columna,actual.dato.token, actual.dato.descripcion))
            actual = actual.siguiente
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////
    def analizar(self):
        self.compilar.compila(self.texto_izquierdo.get(1.0,END))
        if self.compilar.compilar.lista_errores.tamaño > 0 or self.compilar.compilar.lista_errores.tamaño==0:

            self.texto_derecho.delete(1.0,[END])
            self.texto_derecho.insert(1.0,self.compilar.doc)

    def obtener(self):
        self.texto_derecho.delete(1.0, [END])
        texto = self.texto_izquierdo.get(1.0, [END])
        self.texto_derecho.insert(1.0, texto)

    def Salir(self):
        self.pantalla_principal.destroy()    

    def Abrir(self):
        try:
            self.file = askopenfilename(title='Cargar Archivo',filetypes=[("Archivos", f'*')])
            abrir = open(self.file)
            archivo = abrir.read()
            self.texto_izquierdo.delete(1.0,END)
            self.texto_izquierdo.insert(1.0, archivo)
        except:
            tkinter.messagebox.showerror('Guardado', 'Ningpun archivo cargado')

    def Nuevo(self):
        texto = self.texto_izquierdo.get(1.0,[END])
        if texto == None or texto=='':
            self.texto_izquierdo.delete(1.0,[END])
        if texto!='':
            self.GuardarComo()

    def Guardar(self):
        text = self.texto_izquierdo.get(1.0,[END])
        fichero = open(self.file,'w+')
        fichero.write(text)
        fichero.close()

    def GuardarComo(self):
        nuevo_Archivo = asksaveasfile(title='Guardar Archivo Como', filetypes=(('Archivos', '*'),))
        if nuevo_Archivo:
            texto = self.texto_izquierdo.get(1.0,[END])
            nuevo_Archivo.write(texto)
            nuevo_Archivo.close()


gui = Interfaz()