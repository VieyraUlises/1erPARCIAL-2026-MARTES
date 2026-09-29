# Algoritmos y Estructuras de Datos

# 1erPARCIAL - MARTES - 29/09/26 - Comisión 1 -



- - -

### 📌 **Modalidad**

* 🗓️ **Fecha:** Martes **29/09**
* 🕖 **Disponibilidad:** desde las **08:30 hs** hasta las **14:15 h**.
* ⏱️ **Duración máxima:** **3 horas y 30 minutos (3:30 h)** desde el momento en que bifurcan el repositorio.
* 🧪 **Intentos:** Solo **1 (uno)**. 
* 📢 **Publicación de notas:** a más tardar el **Jueves posterior, después de las hs**.

> ⚠️ **IMPORTANTE:** deben estar conectados al Meet, **SE CONSIDERAN AUSENTES AQUELLOS/AS ALUMNOS/AS QUE NO SE CONECTEN**

> ⚠️ **IMPORTANTE:** Al final del archivo `README.md`, **DEBEN completar sus datos personales** (nombre completo, número de legajo y correo institucional).


- - -

# La Vida en el Apartamento 4A

- - -

## (1pt.) Ejercicio 1: La Serie de Potencias de Sheldon

Generar un conjunto por compresión que contenga los números racionales que son potencia de 3, comenzando por el 1 y terminando en 0. 

<u>Ejemplo:</u> <code>{ 1, 1/3, 1/9, 1/27, ... }</code>

---

## (3pt.) Ejercicio 2: La Biblioteca de Sheldon

Crear una clase <code>Biblioteca</code>. Una biblioteca es una colección homogénea y ordenada de libros (pueden utilizar una lista para representarla). 
La clase debe contener métodos para facilitar:

    - Crear una biblioteca vacía.
    - Identificar si una biblioteca está vacía o no.
    - Añadir y remover libros de la biblioteca.

<u>Importante:</u> Pueden agregar más atributos y métodos, si lo consideran necesario.

---

## (2pt.) Ejercicio 3: La Organización de la Biblioteca

Añadir a la clase <code>Biblioteca</code> los siguientes métodos:

    - leer_primer_libro()
    - leer_ultimo_libro()
    - insertar_al_principio()
    - agregar_al_final()

*<u>Nota:</u> pensar en los parámetros que necesita cada método para realizar su trabajo y qué operación debe realizar.*

---

## (2pt.) Ejercicio 4: La Representación de la Biblioteca

Sobrescribir los métodos <code>\_\_len\_\_</code>, <code>\_\_str\_\_</code>, <code>\_\_eq\_\_</code>, y <code>\_\_add\_\_</code> de la clase Biblioteca.

---

## (1pt.) Ejercicio 5: El Conteo de Libros de Leonard (Iterativo)

Implementar una función *iterativa* que calcule la cantidad total de libros en una biblioteca (de la clase <code>Biblioteca</code> definida con anterioridad).

---

## (1pt.) Ejercicio 6: El Conteo de Libros de Penny (Recursivo)

Implementar una función *recursiva* que calcule la cantidad total de libros en una biblioteca (de la clase <code>Biblioteca</code> definida con anterioridad).

---

## (2pt.) Ejercicio 7: El Inventario de Comics de Stuart

Definir una clase <code>Comic</code> que represente un cómic en venta en la tienda de Stuart. Contiene los datos:
*   <code>titulo</code>: 'string'
*   <code>id_comic</code>: 'integer'
*   <code>fecha_publicacion</code>: `date` (importar `datetime`)
*   <code>precio</code>: 'float'
*   <code>stock</code>: 'integer'

La clase debe contener métodos para facilitar:
*   Cambiar uno o varios datos del cómic (título, precio, stock).
*   Calcular en cuántos días se publicó un cómic desde una fecha de referencia. Si el método detecta que el cómic es más antiguo que la fecha de referencia, deberá informar al usuario y marcar el stock como 0.

---

## (2pt.) Ejercicio 8: La Etiqueta de los Comics (Sobrecarga de Métodos)

Sobrecargar los siguientes métodos en la clase <code>Comic</code>:
*   <code>\_\_str\_\_</code>: Para representar el cómic de forma legible (ej: "Comic: The Flash #1 | ID: 456 | Precio: $5.99 | Stock: 25").
*   <code>\_\_eq\_\_</code>: Para comparar si dos cómics son iguales basándose en su <code>id_comic</code> y <code>titulo</code>.

---

## (2pt.) Ejercicio 9: La Gestión de la Tienda de Comics

Crear una clase <code>TiendaComics</code>, la cual estará representada mediante varias listas de objetos del tipo <code>Comic</code>. Cada lista corresponde a una sección de la tienda (ej: "DC Comics", "Marvel", "Independientes").

La clase debe contener métodos para facilitar:
*   Controlar el stock de cómics (añadir un nuevo cómic a una sección, remover un cómic del inventario, actualizar stock).
*   Calcular cuántos cómics tienen stock crítico (menor o igual a 3) y removerlos del inventario (simulando que Stuart los retira por falta de demanda).

---

## (2pt.) Ejercicio 10: La Gestión con Listas Enlazadas

10.1 Se deberán implementar las listas utilizadas en las clases definidas anteriormente utilizando Listas Enlazadas. Encontrarán el prototipo en su archivo correspondiente.

10.2 Implementar Iteradores para las listas enlazadas.

---

### Por Favor Completar sus Datos


<u>**Nombre y Apellido:**</u> Ulises Vieyra

<u>**Email:**</u> uliivieyra@gmail.com

<u>**Comisión:**</u> 03

---