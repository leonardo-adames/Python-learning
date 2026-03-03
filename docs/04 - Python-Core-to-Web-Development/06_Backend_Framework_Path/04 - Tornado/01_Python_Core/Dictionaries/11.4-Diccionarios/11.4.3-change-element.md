# BootCamp Python Sesión 11- Tipos De Datos Compuestos O Colección (Los Diccionarios `dict`)

## 11.4.2 Cambiar elementos del diccionario en python

## Cambiar valores

Puede cambiar el valor de un elemento específico consultando su nombre de clave:

### Ejemplo

Cambie el "año" a 2018:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
```

## Actualizar diccionario

El método `update()` actualizará el diccionario con los elementos del argumento dado.<br>
El argumento debe ser un diccionario o un objeto iterable con pares clave:valor.

### Ejemplo

Actualice el "año" del automóvil utilizando el método `update()`:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
```
