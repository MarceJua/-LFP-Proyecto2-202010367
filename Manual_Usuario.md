# LABORATORIO LENGUAJES FORMALES Y DE PROGRAMACION
## Proyecto 2
### Primer Semestre 2024
```js
Universidad San Carlos de Guatemala
Programador: Marcelo André juarez Alfaro
Carne: 202010367
Correo: mjuarez2017ig@gmail.com
```
---
## Propósito

### Nombre del Software: Analizador Sintáctico para una Base de Datos 
### Número de versión/release: Versión 1.0

El propósito de este documento es proporcionar una visión general completa del Analizador Sintáctico para una Base de Datos. Cubre todos los aspectos relevantes relacionados con los requerimientos de software, las funcionalidades y las características planificadas del sistema. El objetivo principal consiste en el desarrollo de un analizador sintáctico para un lenguaje específico utilizado en la manipulación de una base de datos no relacional. El analizador sintáctico se encarga de verificar la corrección gramatical y semántica de las consultas y comandos escritos en dicho lenguaje.

## Alcance del producto/ Software
El programa está diseñado para analizar sintácticamente consultas y comandos escritos en un lenguaje específico utilizado para interactuar con bases de datos no relacionales.
Puede identificar la estructura gramatical de las consultas ingresadas y validar su corrección sintáctica.

## Funcionalidades del Programa
El programa PetManager ofrece una variedad de funcionalidades diseñadas para la gestión y el cuidado de gatos virtuales. Estas funcionalidades incluyen:

* Análisis Sintáctico de Consultas:
    * El programa puede analizar sintácticamente consultas y comandos escritos en un lenguaje específico utilizado para interactuar con bases de datos no relacionales.
    * Identifica la estructura gramatical de las consultas ingresadas y valida su corrección sintáctica.
* Identificación de Errores de Sintaxis:
    * Detecta y señala errores de sintaxis en las consultas ingresadas, como uso incorrecto de tokens, estructuras inválidas o discrepancias semánticas.
    * Proporciona mensajes de error claros y descriptivos para ayudar al usuario a entender y corregir los problemas detectados.
* Generación de Resultados de Análisis:
    * Después de analizar una consulta, el programa genera resultados que muestran los tokens reconocidos, los errores encontrados y, opcionalmente, la traducción del código a instrucciones ejecutables.
    * Estos resultados se presentan de manera organizada y legible en la interfaz gráfica del programa.
* Interfaz Gráfica Intuitiva:
    * Proporciona una interfaz gráfica de usuario (GUI) intuitiva y fácil de usar que permite a los usuarios cargar consultas, ver resultados de análisis, guardar archivos y acceder a otras funciones con facilidad.
    * La interfaz está diseñada con elementos visuales claros y controles bien definidos para mejorar la experiencia del usuario.
* Compatibilidad Multiplataforma:
    * El programa es compatible con varios sistemas operativos, lo que permite su utilización en entornos informáticos con diferentes configuraciones.
    * Los usuarios pueden ejecutar el software en sistemas Windows, Linux y macOS sin problemas de compatibilidad.
* Opciones de Guardado y Carga de Archivos:
    * Permite a los usuarios guardar consultas y resultados de análisis en archivos locales para su posterior referencia.
    * También ofrece la capacidad de cargar archivos previamente guardados para reanudar el trabajo anterior o compartir consultas con otros usuarios.
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

## Requerimientos de interfaces externas  
A continuación, se describirá las funcionalidades con las cuales cuenta el 
proyecto, estas incluyen una imagen del programa y una descripción breve 
de como esta funciona.
* Pestaña Archivo
    * Se tienen diferentes opciones como:
        * Nuevo: Limpia el área de edición de código, en la cual el usuario puede editar sus sentencias. Si existe un archivo abierto deberá preguntar si desea guardar los cambios antes de limpiar el editor
        * Abrir: Permite abrir un archivo ya creado previamente que contiene las 
        sentencias que generar los comandos de MongoDB
        * Guardar: Permite guardar el código que se está escribiendo actualmente
        * Guardar Como: Esta opción permite guardar el código de las sentencias 
        que se está editando con otro nombre. 
        * Salir: Cierra el programa
![arch](https://i.ibb.co/Dt4xXN9/arch.png)

* Pestaña Tokens
    * Muestra una tabla que enumera todos los tokens encontrados durante el análisis del código fuente ingresado por el usuario. Cada token se presenta con su correspondiente lexema.
![token](https://i.ibb.co/bmy1Ybs/token.png)

* Pestaña Errores
    * Muestra una tabla que lista todos los errores encontrados durante el proceso de análisis del código fuente ingresado por el usuario. Cada error se presenta con detalles como el tipo de error, la línea y columna donde ocurrió, el token esperado y una descripción del error.
![error](https://i.ibb.co/3k30csm/error.png)

* Botón Analizar
    *  Inicia el proceso de análisis del código fuente ingresado por el usuario. Al hacer clic en este botón, el programa ejecutará el análisis léxico y sintáctico del código para identificar tokens y errores, respectivamente.
![analiza](https://i.ibb.co/p4YqJMT/analiza.png)

* Cuadro de Texto Izquierdo
    *  Área donde los usuarios pueden ingresar o editar el código fuente que desean analizar. Este cuadro de texto es utilizado para ingresar el código que se someterá al proceso de análisis léxico y sintáctico.

* Cuadro de Texto Derecho
    *  Área donde se muestran los resultados del análisis realizado en el código fuente. Aquí se presentan los tokens identificados y cualquier error sintáctico detectado durante el proceso de análisis.

## Requerimientos no funcionales
* Rendimiento:
    * El sistema debe ser capaz de manejar grandes volúmenes de datos de manera eficiente, garantizando tiempos de respuesta rápidos incluso en situaciones de carga máxima.
    * La generación de sentecnias MOngDB, tablas de token y Error debe ser rápida y no debe afectar significativamente el rendimiento general del sistema.

* Usabilidad:
    * La interfaz de usuario debe ser intuitiva y fácil de usar para la generacion de sentencias MongoDB.
    * El sistema debe ser accesible desde múltiples dispositivos y plataformas, incluyendo computadoras de escritorio, dispositivos móviles y tabletas.