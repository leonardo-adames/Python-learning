
# BootCamp Python Sesión 7 - Caracteres de escape

## 7.3 Personaje de escape en python

* Para insertar caracteres ilegales en una cadena, utiliza un carácter escape.

* Un personaje de escape es una barra diagonal seguida del personaje que quieres insertar.`\`

* Un ejemplo de carácter ilegal es una doble comilla dentro de una cadena rodeada de comillas dobles:

Ejemplo

* Obtendrás un error si usas comillas dobles dentro de una cadena que es Rodeado de comillas dobles:

```python
txt = "We are the so-called "Vikings" from the north."
```

* Para solucionar este problema, usa el carácter escape :`\"`

Ejemplo

El carácter escape te permite usar comillas dobles cuando normalmente no te dejarían:

```python
txt = "We are the so-called \"Vikings\" from the north."
```

# Personajes de escape

Otros caracteres de escape usados en Python:

|Code	       |Result            |
|-------|-------------------------|	
|\'	           |Single Quote      |
|\\	           |Backslash	      |
|\n	           |New Line	      |
|\r	           |Carriage Return   |	
|\t	           |Tab	              |
|\b	           |Backspace	      |
|\f	           |Form Feed	      |
|\ooo	       |Octal value	      |
|\xhh	       |Hex value         |