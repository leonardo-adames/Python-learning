# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (`Las Tuplas`)

## 11.2.1 `Tuplas` en python

```python
mytuple = ("apple", "banana", "cherry")
```

### Introducción

Las `tuplas` son una colección ordenada e inmutable de elementos en Python. Se definen utilizando paréntesis `()` y los elementos se separan por comas. A diferencia de las listas, las tuplas no pueden ser modificadas después de su creación, lo que las hace ideales para datos que deben permanecer constantes.

`Tuple` es uno de los 4 `tipos de datos integrados` en Python que se utilizan para almacenar colecciones de los otros 3 son `Lista`, `Set` y `Diccionario`, todos con diferentes cualidades y usos.

Una tupla es una colección ordenada e inmutable.

Las tuplas se escriben entre Paréntesis, Ejemplo:

### Tupla básica

```python
mi_tupla = (1, 2, 3)
```

#### Tupla sin paréntesis (packing)

```python
otra_tupla = 4, 5, 6
```

### Tupla de un solo elemento (requiere una coma)

```python
#esta es una tupla de un item
tupla_un_elemento = (7,)

#Esto no es  una tupla de un ítem, recuerda la coma:
thistuple = (7)
print(type(thistuple))
```

### Acceso a Elementos

Los elementos de una tupla se acceden mediante índices, comenzando desde 0:

```python
mi_tupla = (10, 20, 30)
print(mi_tupla[0]) # Resultado: 10
print(mi_tupla[-1]) # Resultado: 30
```

### Desempaquetado de Tuplas

El desempaquetado permite asignar los valores de una tupla a variables individuales:

```python
mi_tupla = ("Luis", "Perez", 30)
nombre, apellido, edad = mi_tupla
print(nombre) # Resultado: Luis
```

También puedes usar el operador `*` para agrupar elementos:

```python
cabeza, *cola = (1, 2, 3, 4)
print(cabeza) # Resultado: 1
print(cola) # Resultado: [2, 3, 4]
```

### Métodos de las Tuplas

Las tuplas tienen métodos limitados debido a su inmutabilidad:

```python
mi_tupla = (1, 2, 2, 3)
print(mi_tupla.count(2)) # Cuenta las ocurrencias de un elemento
print(mi_tupla.index(3)) # Devuelve el índice del primer elemento encontrado
```

### Conversión entre Listas y Tuplas

Puedes convertir listas a tuplas y viceversa:

```python
mi_lista = [1, 2, 3]
mi_tupla = tuple(mi_lista) # Convierte lista a tupla
print(mi_tupla)
otra_lista = list(mi_tupla) # Convierte tupla a lista
print(otra_lista)
```

### Elementos de tuplas

    Los elementos de tupla están ordenados, son inmutables y permiten valores duplicados.

    Los elementos de tuplas están indexados, el primero tiene índice, el segundo tiene índice, etc.[0][1]

### Ordenado

    Cuando decimos que las tuplas están ordenadas, significa que los elementos tienen un orden definido, y ese orden no cambiará.

### Inmutable

    Las tuplas son inalterables, lo que significa que no podemos cambiar, añadir ni eliminar elementos una vez que la tupla ha sido creada.

### Permitir duplicados

    Dado que las tuplas están indexadas, pueden tener elementos con el mismo valor:

### Ejemplo

Las tuplas permiten valores duplicados:

```python
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
```

### Longitud de la tupla

Para determinar cuántos elementos tiene una tupla, utiliza la función:`len()`

### Ejemplo

Imprime el número de elementos en la tupla:

```python
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
```

### Elementos Tupla - Tipos de datos

Los elementos de la tupla pueden ser de cualquier tipo de dato:

### Ejemplo

Tipos de datos de cadena, int y booleanos:

```python
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
```

Una tupla puede contener diferentes tipos de datos, aquí ana tupla con c`adenas`, `enteros` y `valores booleanos`:

```python
tuple1 = ("abc", 34, True, 40, "male")
```

### type()

Desde la perspectiva de Python, las tuplas se definen como objetos con el tipo de dato `'tuple'`:

```python
<class 'tuple'>
```

### Ejemplo

**¿Cuál es el tipo de dato de una tupla?**

```python
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
```

### El constructor de tuple()

También es posible usar el constructor tuple() para crear una tupla.

### Ejemplo

Usando el método `tuple()` para crear una tupla:

```python
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
```

### Ventajas de las Tuplas

**`Inmutabilidad:`** Protege los datos de modificaciones accidentales.

**`Eficiencia:`** Ocupan menos memoria que las listas.

**`Hashables:`** Pueden usarse como claves en diccionarios.

**`Ordenadas:`** Mantienen el orden de los elementos.

Las tuplas son ideales para representar datos constantes, como coordenadas, configuraciones o claves en estructuras de datos.

### Colecciones de Python (Arrays)

Existen cuatro tipos de datos de colección en el lenguaje de programación Python:

* **List** es una colección ordenada y cambiable. Permite miembros duplicados.
* **Tupla** es una colección ordenada e inmutable. Permite miembros duplicados.
* **Set** es una colección que no está ordenada, inmutable, y sin indexar. No hay miembros duplicados.
* **Diccionario** es una colección que se ordena y cambiantes. No hay miembros duplicados.

*Los elementos de los conjuntos son inmutables, pero puedes eliminar y/o añadir elementos Cuando quieras.*

*A partir de la versión 3.7 de Python, los diccionarios están ordenados. En Python 3.6 y anteriores, los diccionarios no están ordenados.*

Al elegir un tipo de colección, es útil entender las propiedades de ese tipo. Elegir el tipo adecuado para un conjunto de datos concreto puede significar retener el significado y, de hecho, un aumento en la eficiencia o la seguridad.

### **TODO LO ANTERIOR MENCIONADO ES UNA BREVE INTRODUCCIÓN A LOS TEMAS QUE VEREMOS ACONTINUACIÓN**
