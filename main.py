from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfile
import tkinter.messagebox
from ttkthemes import ThemedStyle
from AnalizadorSintactico import *

class Interfaz:
    def __init__(self):
        self.pantalla_principal = Tk()
        self.pantalla_principal.geometry('1100x600')
        self.pantalla_principal.title("Analizador")
        self.pantalla_principal.config(bg='#f0f0f0')
        style = ThemedStyle(self.pantalla_principal)
        style.set_theme("arc")
        self.componenentes()
        self.menu()
        
        self.archivo_abierto = None
        self.pantalla_principal.mainloop()

    def componenentes(self):
        encabezado = Label(self.pantalla_principal, text="LFP - Proyecto 2", font=('Helvetica', 20), bg='#f0f0f0')
        encabezado.place(x=500, y=30)

        # cuadro de texto derecho
        self.texto_derecho = Text(self.pantalla_principal)
        self.texto_derecho.config(height=25, width=50, bg='#FFFACD', border=0, fg='#000000', 
                                  insertbackground='black', font=('Helvetica',12), padx=11)
        self.texto_derecho.place(x=600,y=90)
        
        # cuadro de texto izquierdo
        self.texto_izquierdo = Text(self.pantalla_principal)
        self.texto_izquierdo.config(height=25, width=50, bg='#FFFACD', border=0, fg='#000000',
                               insertbackground='black', font=('Helvetica', 12), padx=11, wrap='word')
        self.texto_izquierdo.place(x=100,y=90)           
        
        Analizar = Button(self.pantalla_principal, text='Analizar', font=('Helvetica', 12), command=self.analizar,
                      bg='#FFFACD', fg='black') 
        Analizar.place(x=20, y=90)
    
    #/
    def menu(self):
        self.menu1 = Menu(self.pantalla_principal)
        self.menu1.config(bg='#f0f0f0')
        #--------------------------------------------
        self.filemenu = Menu(self.menu1, tearoff=0)
        self.filemenu.add_command(label='Nuevo', command=self.Nuevo)
        self.filemenu.add_command(label='Abrir', command=self.Abrir)
        self.filemenu.add_command(label='Guardar', command=self.Guardar)
        self.filemenu.add_command(label='Guardar Como', command=self.GuardarComo)
        self.filemenu.add_command(label='Salir', command=self.Salir)
        #--------------------------------------------
        self.ayuda_menu = Menu(self.menu1, tearoff=0)

        opcion1 = self.menu1.add_cascade(label='Archivo', menu=self.filemenu)
        opcion3 = self.menu1.add_command(label='Tokens', command=self.TablaTokens)
        opcion4 = self.menu1.add_command(label='Errores', command=self.TablaErrores)
        #opcion5 = self.menu1.add_cascade(label='Ayuda', menu=self.ayuda_menu)

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
            print(actual.dato.Token+ '     ->    ' +actual.dato.Lexema)
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
    #/
    
    def analizar(self):
        self.compilar = Sintactico() #
        self.compilar.compila(self.texto_izquierdo.get(1.0,END))
        if self.compilar.compilar.lista_errores.tamaño > 0 or self.compilar.compilar.lista_errores.tamaño==0:
            #self.compilar.Sintactico()
            self.texto_derecho.delete(1.0,[END])
            self.texto_derecho.insert(1.0,self.compilar.doc)
            
        self.compilar.lista.imprimir()

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
        # Si hay un archivo abierto, preguntar si desea guardar los cambios
        if self.archivo_abierto:
            if tkinter.messagebox.messagebox.askyesno("Guardar cambios", "¿Desea guardar los cambios antes de abrir un nuevo archivo?"):
                self.Guardar()
        
        # Limpiar el área de edición
        self.texto_izquierdo.delete('1.0', 'end')
        self.archivo_abierto = None  # Resetea el nombre del archivo abierto

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


inter = Interfaz()