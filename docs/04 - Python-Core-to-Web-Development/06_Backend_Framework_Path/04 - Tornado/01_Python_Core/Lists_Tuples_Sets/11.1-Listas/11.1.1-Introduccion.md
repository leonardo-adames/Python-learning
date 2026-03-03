# BootCamp Python Sesión 101- Tipos De Datos Compuestoso  De Colección (`Las listas`)

## 11.1.1 `Listas` en python

### ¿Qué es?

Las listas se utilizan para almacenar varios elementos en una sola `variable`.

Las listas son uno de los 4 `tipos de datos integrados` en Python que se utilizan para almacenar `colecciones` de los otros 3 son `Tupla`, `Set` y `Dictionario`, todos con diferentes cualidades y usos.

En Python, las `listas` son estructuras de datos fundamentales que permiten almacenar colecciones ordenadas y mutables de elementos.

Para crear una lista, se utilizan corchetes `[]` y los elementos se separan por comas `,`.

### NOTA

Si los elementos a almacenar son string (`"cadenas de texto"` o `"cuerda"`)
se colocan entre doble comillas,

si los elementos son numeros enteros (`int`), Números decimales (`folat`) O Complejos (`complex`) estos se agregan tal cual, es decir, sin estar entre comillas o parentesis solo separados por comas.

### Ejemplo

**Crea una lista:**

```python
lista = ["apple", "banana", "cherry"]   # ESTA ES UNA LISTA
print(lista)
```

### Elementos de la lista

Los elementos de la lista están ordenados, son modificables y permiten valores duplicados.

Los elementos de la lista están indexados, el primer elemento tiene índice , El segundo elemento tiene índice, etc. `[0]` `[1]`

### Ordenado

Cuando decimos que las listas están ordenadas, significa que los elementos tienen un orden definido, y ese orden no cambiará.

Si añades nuevos elementos a una lista, Los nuevos elementos se colocarán al final de la lista.

Nota: Existen algunos métodos de lista que cambian el orden, pero en general: el orden de los elementos no cambia.

### Cambiantes

La lista es cambiable, lo que significa que podemos cambiar, añadir y eliminar elementos de una lista una vez creada.

### Permitir duplicados

Como las listas están indexadas, las listas pueden tener elementos con el mismo valor:

### Ejemplo

**Las listas permiten valores duplicados:**

```python
thislist = ["apple", "banana", "cherry", "apple", "cherry"] # cherry aparece 2 veces
print(thislist)
```

En python tamnién se pueden crear `listas complejas`, estas no son más, que un conjunto de diferente tipos de colecciones dentro de una ola lista, por ejemplo:

```python
usuario = ["leonardo",                          # string (cadena de texto o cuerda)
        25,                                     # int (entero)
        True,                                   # bool (Booleano)
        [85, 90, 95],                           # list (lista anidada o interna, lista dentro de una lista)
        {"pais": "rd", "nivel": "avanzado"},    # dict (Diccionario anidado o interno, diccionario dentro de una lista)
        (3, 4, 5)]                              # tuple (Tupla anidada o interna, tupla dentro de  una lista)
```

En este ejemplo vemos que hay una lista llamada `usuario` con varios elementos y colecciones dentro de ella (Dentro de ella hay: `Listas`, `tTuplas`, `Dicionarios`).

### type()

Desde la perspectiva de Python, las listas se definen como objetos con el tipo de dato 'lista':

`<class 'list'>`

### Ejemplo

¿Cuál es el tipo de dato de una lista?

```python
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
```

RESULTADO:

```python
<class 'list'>
```

### El constructor list()

También es posible usar el constructor `list()` al crear un nueva lista.

### Ejemplo

Usando el constructor para hacer una lista: `list()`

```python
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
```

### Colecciones de Python (Arrays)

Existen cuatro tipos de datos de colección en el lenguaje de programación Python:

`List` es una colección ordenada y cambiable. Permite miembros duplicados.
`Tupla` es una colección ordenada e inmutable. Permite miembros duplicados.
`Set` es una colección que no está ordenada, inmutable*, y sin indexar. No hay miembros duplicados.
`Diccionario` es una colección que se ordena** y cambiantes. No hay miembros duplicados.

Los elementos de los conjuntos son inmutables, pero puedes eliminar y/o añadir elementos Cuando quieras.

**A partir de la versión 3.7 de Python, los diccionarios están ordenados. En Python 3.6 y anteriores, los diccionarios no están ordenados.**

Al elegir un tipo de colección, es útil entender las propiedades de ese tipo. Elegir el tipo adecuado para un conjunto de datos concreto puede significar retener el significado y, de hecho, un aumento en la eficiencia o la seguridad.
