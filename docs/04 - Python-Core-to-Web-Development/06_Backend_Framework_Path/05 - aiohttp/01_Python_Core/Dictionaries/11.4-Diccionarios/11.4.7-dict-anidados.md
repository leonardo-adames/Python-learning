# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (Los Diccionarios `dict`)

## 11.4.7 Diccionarios Anidados en python

### Copiar un Diccionario<br>
Diccionarios anidados
Un diccionario puede contener diccionarios, esto se llama diccionarios anidados.

### Ejemplo

```python
Crea un diccionario que contenga tres diccionarios:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
```
**O, si desea agregar tres diccionarios en un nuevo diccionario:**

### Ejemplo<br>
**Crea tres diccionarios y luego crea un diccionario que contendrá los otros tres diccionarios:**
```python
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
```

## Acceder a elementos en diccionarios anidados

Para acceder a los elementos de un diccionario anidado, utilice el nombre de los diccionarios, comenzando con el diccionario externo:

### Ejemplo

**Imprima el nombre del niño 2:**

```python
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])
```
---
## Recorrer diccionarios anidados

Puedes recorrer un diccionario usando el items()siguiente método:

### Ejemplo<br>
Recorrer las claves y valores de todos los diccionarios anidados:

```python
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
```
