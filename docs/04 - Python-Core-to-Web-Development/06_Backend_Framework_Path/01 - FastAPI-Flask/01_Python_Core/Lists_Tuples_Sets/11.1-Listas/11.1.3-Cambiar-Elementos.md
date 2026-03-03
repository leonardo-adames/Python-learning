# BootCamp Python Sesión 101- Tipos De Datos Compuestoso  De Colección (`Las listas`)

## 11.1.3 `Cambiar Elementos De Una Listas` en python

### Cambiar el valor del objeto

Para cambiar el valor de un artículo específico, Consulte el número de índice:

### Ejemplo

Cambia el segundo punto:

```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
```

### Cambiar un rango de valores de objetos

Para cambiar el valor de los elementos dentro de un rango específico, define una lista con los nuevos valores y consulta el rango de números de índice donde quieres insertar los nuevos valores:

### Ejemplo

Cambia los valores "plátano" y "cereza" por los valores "grosella negra" y "sandía":

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
```

Si insertas más elementos de los que reemplazas, los nuevos elementos se insertarán donde lo especificaste y los objetos restantes se moverán en consecuencia:

### Ejemplo

Cambia el segundo valor reemplazándolo por dos nuevos Valores:

```python
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
```

**Nota:** La longitud de la lista cambiará cuando el número de elementos insertados no coincida con el número de elementos reemplazados.

Si insertas menos elementos de los que reemplazas, los nuevos elementos se insertarán donde lo especificaste y los objetos restantes se moverán en consecuencia:

### Ejemplo

Cambia el segundo y tercer valor reemplazándolo por un solo valor:

```python
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
```

### Método `insert`

Para insertar un nuevo elemento de lista, sin reemplazar ninguno de los valores existentes, podemos usar el método.`insert()`

El método inserta un ítem en el índice especificado:insert()

### Ejemplo

```python
Inserta "sandía" como tercer elemento:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
```

**Nota:** Como resultado del ejemplo anterior, la lista ahora contendrá 4 elementos.
