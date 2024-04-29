# LABORATORIO LENGUAJES FORMALES Y DE PROGRAMACION
## Proyecto 2
### Primer Semestre 2024
```js
Universidad San Carlos de Guatemala
Programador: Marcelo André Juarez Alfaro
Carne: 202010367
Correo: mjuarez2017ig@gmail.com
```
---
## Descripción del Proyecto
El proyecto consiste en el desarrollo de un analizador sintáctico para un lenguaje específico utilizado en la manipulación de una base de datos no relacional. El analizador sintáctico se encarga de verificar la corrección gramatical y semántica de las consultas y comandos escritos en dicho lenguaje.

## Objetivos
* Objetivo General
    * Combinar los conocimientos adquiridos en el curso y en los otros cursos de 
sistemas, para crear un compilador que traduzca el lenguaje especificado y lo 
transforme en Sentencias de Bases de Datos No Relacionales.
* Objetivos Específicos
    * Crear una herramienta que permita el diseño de sentencias de base de datos 
    no relacionales de una forma sencilla para el usuario. 
    * Diseñar y construir un compilador que permita compilar archivos de entrada 
    y visualizar el resultado en un entorno externo.
    * Desarrollar la habilidad del estudiante para elaborar proyectos en base a una 
    adecuada planificación para que aprendan la manera en la que tienen que 
    trabajar.


## Funcionalidades del Programa
El programa ofrece una variedad de funcionalidades diseñadas para la gestión y el cuidado de gatos virtuales. Estas funcionalidades incluyen:

* Análisis Sintáctico Avanzado:
    * El programa cuenta con un analizador sintáctico avanzado que puede identificar y validar la estructura gramatical de las consultas y comandos ingresados en el lenguaje específico para la base de datos no relacional.
    * Realiza un análisis exhaustivo de la sintaxis, identificando errores de formato, uso incorrecto de tokens y discrepancias semánticas.

* Generación de Resultados Claros y Detallados:
    * Después del análisis sintáctico, el programa genera resultados claros y detallados que muestran los tokens reconocidos, los errores encontrados y, opcionalmente, la traducción del código a instrucciones ejecutables.
    * Los resultados se presentan de forma organizada y fácil de interpretar, lo que facilita la identificación y corrección de posibles problemas en el código.

* Interfaz Gráfica Intuitiva:
    * La interfaz gráfica del programa proporciona una experiencia de usuario intuitiva y amigable, que permite a los usuarios interactuar de manera efectiva con el sistema.
    * Ofrece funciones como carga de archivos, guardado de resultados, visualización de tablas de tokens y errores, todo ello mediante una disposición clara y accesible de botones, menús y opciones.

* Documentación Detallada y Soporte Técnico:
    * Se proporciona una documentación completa del programa, que incluye descripciones detalladas de las funcionalidades, instrucciones de uso, ejemplos de código y referencias útiles.

## Entorno Operativo
El sistema se desarrollará para funcionar en computadoras de escritorio 
convencionales.

Se requiere un hardware típico de oficina, que incluye una CPU con al menos 
un procesador de doble núcleo, 8 GB de RAM y 10 GB de espacio de disco 
duro para el almacenamiento de datos y el software del sistema.

El sistema de desarrollará principalmente para funcionar con sistemas 
operativos Windows (10/11).

Se utilizará el lenguaje de programación de Python en todo el proyecto.

Se utilizará entorno de desarrollo integrado (IDE) Visual studio code.

Se utilizó herramientas adicionales de desarrollo, como Git para el control de 
versiones

## Requerimientos funcionales
A continuación, se describirá las funcionalidades con las cuales cuenta el 
proyecto, estas incluyen una imagen del código y una descripción breve 
de como esta funciona.
* Clase Token
    * Permite representar tokens en el analizador léxico. Es una estructura simple que almacena información sobre el tipo de token, su lexema y su posición en el código fuente.
![Class-Token](https://i.ibb.co/Np5WXPv/Class-Token.png)

* Clase ErrorLex:
    * Diseñada para representar errores encontrados durante el análisis léxico o sintáctico.
    ![Class-Err-Lex](https://i.ibb.co/HpJQbgn/Class-Err-Lex.png)
* Clase Lista: ![Class-List](https://i.ibb.co/QcrSYvt/Class-List.png)
    *  clase Analizador que se encarga de analizar el texto de entrada en busca de tokens y errores. La lógica de análisis está dividida en varios métodos como Analizar, Lexemas, comentarioLinea, etc., lo que hace que el código sea modular y fácil de entender.

* Clase AnalizadorLéxico: 
    * Se encarga de analizar el texto de entrada en busca de tokens y errores. La lógica de análisis está dividida en varios métodos como Analizar, Lexemas, comentarioLinea, etc., lo que hace que el código sea modular y fácil de entender.
        * Diccionarios de tokens: Se diseño un diccionario tokens donde se definen los tokens reconocidos y sus equivalentes. Esto permite asignar un nombre descriptivo a los tokens y asociarlos con los lexemas que representan en el código fuente.
![Class-Lex-Dicc](https://i.ibb.co/kXnvV2S/Class-Lex-Dicc.png)
        * Manejo de comentarios: Se implementa la capacidad de reconocer comentarios tanto de una sola línea como de varias líneas. Esto es importante para ignorar los comentarios durante el análisis léxico.
![funjson](https://i.ibb.co/xgKL4Hm/funjson.png)
        * Manejo de errores: Se incluye una lista para almacenar los errores léxicos encontrados durante el análisis. Esto es útil para informar al usuario sobre problemas en el código fuente.
![tokError](https://i.ibb.co/kcScJq4/tokError.png)
        * Reconocimiento de tokens y lexemas: Se utilizan métodos como Lexemas y tokens reconocidos para identificar lexemas y tokens en el texto de entrada. Esto permite construir una lista de tokens válidos para su posterior procesamiento.
![tokRecon](https://i.ibb.co/jzKsSYS/tokRecon.png)
* Clase AnalizadorSintactico:
    * Analizar la estructura sintáctica del código generado por el analizador léxico y generar las sentencias de MongoDB correspondiente.
![Class-Sintact](https://i.ibb.co/RNFJkPF/Class-Sintact.png)
        * Método compila: Este método toma un documento como entrada y utiliza una instancia del analizador léxico (Analizador) para analizarlo.
![compil](https://i.ibb.co/KspcLHH/compil.png)
        * Método Sintactico: Este método es el corazón del analizador sintáctico. Recorre la lista de tokens generada por el analizador léxico y, según las reglas de tu lenguaje, construye las sentencias de MongoDB correspondiente.
![def-Sintact](https://i.ibb.co/4d9MPcc/def-Sintact.png)
        * Métodos específicos para cada función: Se tienen métodos como Crear, Eliminar, CrearCole, etc., que se encargan de generar las sentencias de MongoDB para cada función específica de tu lenguaje. Estos métodos inspeccionan la lista de tokens y construyen sentencias MongoDB. correspondiente según la estructura y los requisitos de las funciones.
![Cre-ELimin](https://i.ibb.co/sCP3x00/Cre-ELimin.png)
        * Manejo de errores: Si una función no sigue la estructura sintáctica esperada, se genera un error sintáctico y se registra en la lista de errores léxicos.
        * Método crearArchivo: Finalmente, este método escribe las sentencias de MongoDB generado en un archivo de salida llamado "Salida.txt".
![creArchv](https://i.ibb.co/hZyZbk9/creArchv.png)

* Clase Interfaz:
![Class-Interfz](https://i.ibb.co/T4GrxwV/Class-Interfz.png)
    * Funcionalidades Básicas:
        * Abrir, Guardar y Guardar como: Permiten al usuario cargar un archivo existente, guardar el contenido actual en un archivo y guardar el contenido actual en un nuevo archivo, respectivamente.
    * Analizar: Esta función asocia a la acción de analizar el código ingresado en el editor de texto izquierdo. Después de analizar el código, muestra los resultados en el editor de texto derecho.
    * Menús y Opciones:
        * Archivo: Contiene opciones para abrir, guardar y salir.
        * Tokens y Errores: Estas opciones parecen mostrar las tablas de tokens y errores respectivamente. La función TablaTokens muestra una tabla con los tokens reconocidos y la función TablaErrores muestra una tabla con los errores encontrados durante el análisis.
    * Interacción con el Usuario:
        * Al seleccionar una opción del menú, se ejecutan las funciones correspondientes.
        * Al hacer clic en el botón "Analizar", se activa la función analizar, que inicia el análisis sintáctico del código ingresado en el editor de texto izquierdo.

# Tabla de tokens

| Token | Descripcion | Patron |
| --- | --- | --- |
| RFUNCION | Palabra reservada CrearBD | CrearBD |
| RFUNCION | Palabra reservada EliminarBD | EliminarBD |
| RFUNCION | Palabra reservada CrearColeccion | CrearColeccion |
| RFUNCION | Palabra reservada EliminarColeccion | EliminarColeccion |
| RFUNCION | Palabra reservada InsertarUnico | InsertarUnico | 
| RFUNCION | Palabra reservada ActualizarUnico | ActualizarUnico |
| RFUNCION | Palabra reservada EliminarUnico | EliminarUnico |
| RFUNCION | Palabra reservada BuscarUnico | BuscarUnico |
| RFUNCION | Palabra reservada BuscarTodo | BuscarTodo |
| RNUEVA | Palabra reservada nueva | nueva |
| RID | Identificador | [a-zA-Z][a-zA-Z0-9] |
| RPARENABIERTO | Parentesis izquierdo | ( |
| RPARENCERRADO | Parentesis derecho | ) |
| RLLAVEABRIR | llave izquierdo | { |
| RLLAVECERRAR | llave derecho | } |
| RCOMA | Caracter Coma | , |
| RASIGNACION | signo igual | = |
| STRING | cadenas de texto, JSON | {  } |
| RPUNTOCOMA | Caracter punto y coma | ; |
| RDOSPUNTOS | Caracter dos puntos | : |
| RCOMILLASDOBLES | Caracter comillas | " |
| RCOMILLASSIMPLES | Caracter comillas | ' |

## Requerimientos no funcionales
* Rendimiento:
    * El sistema debe ser capaz de manejar grandes volúmenes de datos de manera eficiente, garantizando tiempos de respuesta rápidos incluso en situaciones de carga máxima.
    * La generación de sentecnias MOngDB, tablas de token y Error debe ser rápida y no debe afectar significativamente el rendimiento general del sistema.

* Usabilidad:
    * La interfaz de usuario debe ser intuitiva y fácil de usar para la generacion de sentencias MongoDB.
    * El sistema debe ser accesible desde múltiples dispositivos y plataformas, incluyendo computadoras de escritorio, dispositivos móviles y tabletas.

## Expresión Regular
 (S+L* S+| L*)
    Donde:

        S = Símbolos [comillas, parentesis y llaves]
        Letras = L = [a-z A-Z]* = L*

## Método del Árbol

## Automata Finito
![ipc-LFP-automata](https://i.ibb.co/gv94Qk2/ipc-LFP-automata.png)

## Gramática Libre de Contexto

Terminales: {CrearBD, EliminarBD, CrearColeccion, EliminarColeccion, InsertarUnico, ActualizarUnico, EliminarUnico, BuscarUnico, BuscarTodo }
No terminales: {<init>, Instrucciones>, <Instruccion>}
Inicio: <init>

    <init>            : <Instrucciones>

    <Instrucciones>   : <Instruccion> <Instrucciones>
                    | <Instruccion>

    <Instruccion>   : CrearBD ;
                    | EliminarBD ;
                    | CrearColeccion ;
                    | EliminarColeccion ;
                    | InsertarUnico ; 
                    | ActualizarUnico ;
                    | EliminarUnico ;
                    | BuscarUnico ;
                    | BuscarTodo ;

    CrearBD           :: CrearBD identificador = nueva CrearBD ( ) 
    EliminarBD        | EliminarBD identificador = nueva EliminarBD ( )
    CrearColeccion    | CrearColeccion identificador = nueva CrearColeccion ( " STRING " )
    EliminarColeccion | EliminarColeccion identificador = nueva EliminarColeccion ( " STRING " )
    InsertarUnico     | InsertarUnico identificador = nueva InsertarUnico ( " STRING " , " STRINGJSON " )
    ActualizarUnico   | ActualizarUnico identificador = nueva ActualizarUnico ( " STRING " , " STRINGJSON " )
    EliminarUnico     | EliminarUnico identificador = nueva EliminarUnico ( " STRING " , " STRINGJSON " )
    BuscarUnico       | BuscarUnico identificador = nueva BuscarUnico ( " STRING " )
    BuscarTodo        | BuscarTodo identificador = nueva BuscarTodo ( " STRING " )