# proyecto-modulo-3

Proyecto Módulo 3: Control de Inventario 
 
Eva Maria Yared Fox Gomez  
Número de control: 26491034  
26 de octubre de 2026  

El programa debe resolver un problema cotidiano usando estructuras de control de flujo. 
 
El programa debe: 
 
1. Solicitar datos al usuario con input(). 
2. Usar estructuras selectivas (if-elif-else) para tomar decisiones. 
3. Usar estructuras iterativas (while o for) para repetir procesos. 
4. Mostrar resultados con print() y f-strings. 

Presentación: 

Declaración de uso de AI   
Declaro que he utilizado herramientas de IA para buscar información necesaria para llevar acabo el problema de la forma esperada.  
Adjunto los prompts utilizados como evidencia.  
 
Prompt no.1  
Actualmente estoy utilizando una variable llamada mayor = 0 para guardar el precio más alto. ¿Qué otra variable necesitaría para guardar el nombre del producto que tenga ese precio? ¿Cómo debería inicializarla antes de comenzar el ciclo while?

Respuesta de IA   
Puedes utilizar una variable de tipo texto llamada producto_caro e inicializarla con una cadena vacía: 
producto_caro = "" 
Las comillas indican que es una variable de tipo cadena (str). Inicialmente no contiene ningún nombre, pero posteriormente puedes asignarle el nombre del producto que tenga el precio más alto. 
producto_caro = nombre_producto 
 
Prompt no 2  
Además de identificar el producto más caro, quiero que mi programa pueda conservar los nombres y precios de todos los productos que ingrese el usuario. 
No quiero utilizar muchas variables diferentes para guardar cada producto. 
¿Existe alguna manera sencilla de almacenar varios productos con sus respectivos precios utilizando Python? 

Respuesta de IA  
Sí. Puedes utilizar una lista vacía para almacenar varios productos: 
productos = [] 
Los corchetes [] representan una lista vacía. Una lista permite guardar varios elementos dentro de una misma variable. 

Prompt no 3  
Tomando en cuenta que ahora tengo una lista llamada productos = [], 
¿cómo puedo hacer para que cada vez que el usuario ingrese un producto y su precio, ambos datos se guarden dentro de esa lista? 
Quiero que el programa conserve todos los registros mientras el ciclo while sigue funcionando, sin borrar los productos anteriores. 
 
Respuesta IA 
Puedes utilizar el método .append(), que permite agregar un nuevo elemento al final de una lista. 
En tu programa puedes escribir: 
productos.append([nombre_producto, precio]) 
Esto agrega una nueva lista con el nombre y el precio del producto dentro de productos. 
 
Prompt no 4   
¿Existe alguna función de Python que me permita conocer cuántos elementos contiene una lista? 
¿Cómo podría utilizarla dentro de un print con f-string? 

Respuesta IA 
Puedes utilizar la función len(), que permite conocer la cantidad de elementos que contiene una lista. 
Por ejemplo: 
len(productos) 
Si la lista contiene tres productos, el resultado será 3. 
