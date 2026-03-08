<div align="center">
    <kbd><h1><b>CURSO DE PYTHON</b><br>LAS FUNCIONES</b></h1></kbd>
        <img width="2064" height="100%" alt="Image" src="../../../../../notes/resources/INTRO/Py_welcome11.png" altº="Image" width="100%"/>
    <br>
    <br>
    <h2><kbd>DEF FUNCTIONS</kbd></h2>
</div>

<br>

### 1. ¿QUÉ SON?

Las funciones en Python son bloques de código reutilizables que realizan tareas específicas, se definen con `def`, pueden aceptar argumentos y devolver valores con `return`, ayudando a organizar el código, evitar la repetición (principio DRY) y hacerlo más modular y legible. Se llaman simplemente escribiendo su nombre seguido de paréntesis, `nombre_funcion()`, para ejecutarlas.

Las funciones también se denominan `Métodos` cuando se encuentran definidas dentro de una clase.
<br>

### 2. UTILIDAD

-Modularidad: Divide un programa grande en partes pequeñas y manejables.

-Reutilización: Escribes el código una vez y lo usas muchas veces.

-Legibilidad: Hace el código más fácil de entender.

-DRY (Don't Repeat Yourself): Evita escribir el mismo código repetidamente.

---

<br>

### 3. SINTAXIS

sin parametros

```python
def funtion_name():
	instruction

	return(opcional)
```

con parametros

```python
def funtion_name(parametros):
	instruction

	return(opcional)
```
---

<br>

### 4. Definición y estructura

- def: Palabra clave para definir una función.

- Nombre: El identificador único de la función (ej. saludar).

- Paréntesis `()`: Contienen los parámetros (entradas) que la función recibe.

- Dos puntos `:`: Indican el inicio del bloque de código de la función.

- Indentación: El código dentro de la función debe estar indentado (sangrado).

---
<br>

### 5. EJECUCIÓN

LA ejecución se produce a través  de la `Llamada a la función`,
Se ejecuta el código dentro de la función escribiendo su nombre y pasando los argumentos (valores para los parámetros).

**Ejecución de funciónsin parametros:**

```python

def saludar():
    print("Hola, mundo!")

saludar()  # Llamada a la función
```

<br>

### 5.1 Ejecución de funciones con parametros

```python

def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")  # Llamada a la función
```
---

<br>

### 6. Tipos de funciones

- Integradas (Built-in): Funciones que vienen con Python, como print(), len(), type().

- Definidas por el usuario: Las que creas tú mismo con def.

- Recursivas: Funciones que se llaman a sí mismas para resolver problemas complejos.

<br>

## Líneas en blanco

Rodee las definiciones de funciones y clases de nivel superior con dos líneas en blanco.

Las definiciones de métodos dentro de una clase están rodeadas por una sola línea en blanco.

Se pueden usar líneas en blanco adicionales (con moderación) para separar grupos de funciones relacionadas. Se pueden omitir líneas en blanco entre varios scripts de una sola línea relacionados (por ejemplo, un conjunto de implementaciones ficticias).

Utilice líneas en blanco en las funciones, con moderación, para indicar secciones lógicas.

Python acepta el carácter de avance de página Ctrl+L (es decir, ^L) como espacio en blanco; muchas herramientas tratan estos caracteres como separadores de página, por lo que puede usarlos para separar páginas de secciones relacionadas de su archivo. Tenga en cuenta que algunos editores y visores de código web podrían no reconocer Ctrl+L como avance de página y mostrar otro glifo en su lugar.

Te muestro un ejemplo visual en código Python siguiendo las reglas de PEP 8 sobre líneas en blanco. Así puedes ver cómo se aplican en la práctica:

Ejemplo de PEP 8: uso de líneas en blanco

```python
# Así se ve en código


class MiClase:
    def __init__(self, valor):
        self.valor = valor

    def metodo_uno(self):
        # Una línea en blanco separa métodos dentro de la clase
        print("Método uno ejecutado")

    def metodo_dos(self):
        print("Método dos ejecutado")


# Dos líneas en blanco separan definiciones de nivel superior
    def funcion_principal():
    # Se pueden usar líneas en blanco dentro de la función
    # para separar secciones lógicas

    print("Inicio de la función")

    # Sección lógica 1
    datos = [1, 2, 3]
    for d in datos:
        print(d)

    # Sección lógica 2
    resultado = sum(datos)
    print("Suma:", resultado)


def funcion_auxiliar():
    print("Función auxiliar ejecutada") 


# Ejemplo de scripts de una sola línea relacionados (sin líneas en blanco)
x = 1; y = 2; z = 3


# Separador de página con Ctrl+L (puede aparecer como ^L en algunos editores)
# ^L
def otra_funcion():
    print("Nueva sección del archivo")

```
<br>

## 🔎 Explicación visual:

`Dos líneas en blanco` antes de `class MiClase` y `def funcion_principal`.

`Una línea` en blanco entre `métodos` dentro de la `clase`.

`Líneas en blanco` dentro de `funciones` para separar `secciones lógicas` (**Sección lógica 1** y **Sección lógica 2**).

`Scripts de una sola línea` relacionados (`x = 1; y = 2; z = 3`) sin líneas en blanco.

Separador de página `Ctrl+L` o (`^L`) usado para dividir secciones grandes del archivo.
