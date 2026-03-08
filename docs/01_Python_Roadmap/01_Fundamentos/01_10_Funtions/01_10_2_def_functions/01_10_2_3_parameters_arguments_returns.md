<div align="center">
    <kbd><h1><b>CURSO DE PYTHON</b><br>LAS FUNCIONES</b></h1></kbd>
        <img width="2064" height="100%" alt="Image" src="../../../../../notes/resources/INTRO/Py_welcome12.png" altº="Image" width="100%"/>
    <br>
    <br>
    <h2><kbd>DEF FUNCTIONS: PARÁMETROS & ARGUMENTOS</kbd></h2>
</div>

<br>

### ¿QUÉ SON PARÁMETROS DENTRO DE UNA FUNCIÓN EN PYTHON?

En Python, los `parámetros` son las `variables` definidas en la firma de una función (`marcadores de posición`), mientras que los `argumentos` son los `valores` reales pasados al llamarla. La `sintaxis` básica para definir una función con parámetros en Python es la siguiente:

<br>

**`SINTAXIS`**

```PYTHON
def nombre_de_la_funcion(parametro_1, parametro_2, ...):
    # bloque de código de la función que utiliza los parámetros
```
>parametro_1, parametro_2,… son los parámetros de la funcion

#### **`Veamos un ejemplo:`**

```python
#Ejemplo de una función con parámetros
def saludar(nombre): # Parametros
    print("Hola", nombre)

# Llamando a la función con un argumento
saludar("Luis")  # Salida: Hola Luis

```
Aquí definimos una función llamada `saludar` que toma un parámetro llamado `nombre`. Dentro de la función, se imprime un saludo “Hola” seguido del nombre que se pasa como argumento.

Ahora, si llamo a la función con el parámetro `Luis`, esto provoca que la función se ejecute y muestre el mensaje **Hola Luis** como salida.

<br>

### ¿QUÉ SON PARÁMETROS DENTRO DE UNA FUNCIÓN EN PYTHON?

Los `argumentos` son los `valores` reales pasados al llamar la `Función `
**Los argumentos** se asignan a los parámetros por `posición`, por `nombre  (palabras clave)`, o mediante `valores predeterminados`.

<br>

**`SINTAXIS`**

```python
#Definimos una función con parametros y argumentos

def saludar(nombre, edad): #Parametros
    print(f'Hola {nombre}, tu edad es {edad} años')

#Llamamos a la función pasando los argumentos
saludar('Leonardo', 29) #Argumentos

```

**`EXPLICACIÓN RÁPIDA`**

- `nombre` y `edad` son los parámetros de la función(los nombres que usamos para definirlas).

- `'Leonardo'` y `25` son **`Argumentos`** (los valores reales que pasamso al llamar la función `saludar(...)`)

- Cada vez que llames la función (`saludar(...)`), los argumetos reemplazan los parámetros dentro de la sunción
---

<br>

### ¿QUÉ SON VALORES DE RETORNO (**`return`**) DENTRO DE UNA FUNCIÓN EN PYTHON?

Los valores de `retorno` de una función **son un valor que la función puede devolver** (`opcionalmente`) como resultado, después de realizar sus operaciones.

En `Python`, la instrucción `return` se utiliza para devolver un valor desde una función, al punto desde donde se llamó la función.

Cuando se encuentra la instrucción `return`, **la ejecución de la función se detiene** y **el valor especificado después** de `return`se devuelve como resultado de la función.

<br>

**`SINTAXIS`**

```python

def nombre_de_la_funcion(parametros):
    # bloque de código de la función
    return(valor_a_devolver)

```

<br>

**`EJEMPLO PRÁCTICO`**

**Devolver un valor simple**

En su forma más simple, `return` se utiliza para devolver un valor específico desde una función.

```python

def suma(a, b):
    resultado = a + b
    return resultado

# Llamada a la función y asignación del valor devuelto a una variable
resultado_suma = suma(5, 3)
print(resultado_suma)  # Salida: 8

```

<br>

**`OTROS CASOS DE USO DE LA INSTRUCCIÓN RETURN`**

<br>

**Devolver None**

Si una función no tiene una instrucción `return` o si se encuentra `return` sin ningún valor, la función devuelve `None` de forma implícita.

<br>

```python
def funcion_vacia():
    pass

resultado = funcion_vacia()
print(resultado)  # Salida: None
```
---
<br>

#### **Devolver múltiples valores**

`Python` únicamente permite devolver un único valor en un `return`. Pero, el tipo devuelto puede ser de cualquier tipo, lo que incluye agrupaciones de variables.

Podemos usar esto para devolver múltiples valores desde una función utilizando `return`, de devolviendo una tupla, lista o cualquier otro tipo de estructura de datos que contenga los valores a devolver.

**`EJEMPLO PRÁCTICO`**

```python

def calcular_metricas(numeros):
    suma_total = sum(numeros)
    promedio = suma_total / len(numeros)
    valor_maximo = max(numeros)
    
    # Aquí devolvemos una tupla (aunque no usemos paréntesis, Python la crea)
    return suma_total, promedio, valor_maximo

# Datos de prueba
mis_notas = [85, 90, 78, 92]

# "Desempaquetamos" los valores directamente en variables individuales
total, media, nota_alta = calcular_metricas(mis_notas)

print(f"Suma: {total}")
print(f"Promedio: {media}")
print(f"Nota más alta: {nota_alta}")

```

**¿Qué está pasando realmente?**

Cuando escribes `return suma_total, promedio, valor_maximo`, Python hace lo siguiente:

**Empaquetado:** Crea una tupla de forma invisible: (`suma_total, promedio, valor_maximo`).

**Retorno:** Devuelve ese único objeto (la tupla).

**Desempaquetado (`Unpacking`):** Al llamar a la función, puedes asignar esos elementos de la tupla a variables separadas en una sola línea.

<br>


**`Para cerrar este tema con broche de oro, solo recuerda este resumen visual:`**

<div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 20px; color: #e0e0e0;">
  <table style="width: 100%; border-collapse: separate; border-spacing: 0; background-color: #1a1a1a; border-radius: 12px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.4); border: 1px solid #333;">
    <thead>
      <tr style="background: linear-gradient(90deg, #2d6a4f, #52b788);">
        <th style="padding: 15px 20px; text-align: left; color: white; font-weight: 600; text-transform: uppercase; font-size: 13px; letter-spacing: 1.2px; width: 20%;">Acción</th>
        <th style="padding: 15px 20px; text-align: left; color: white; font-weight: 600; text-transform: uppercase; font-size: 13px; letter-spacing: 1.2px; width: 35%;">Código</th>
        <th style="padding: 15px 20px; text-align: left; color: white; font-weight: 600; text-transform: uppercase; font-size: 13px; letter-spacing: 1.2px;">Resultado</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom: 1px solid #333;">
        <td style="padding: 15px 20px; border-bottom: 1px solid #333; font-weight: bold; color: #74c69d;">Llamar y tirar</td>
        <td style="padding: 15px 20px; border-bottom: 1px solid #333;">
          <code style="background: #2d2d2d; padding: 4px 8px; border-radius: 4px; color: #d8f3dc; font-size: 0.9em;">calcular_metricas(mis_notas)</code>
        </td>
        <td style="padding: 15px 20px; border-bottom: 1px solid #333; font-style: italic; color: #95a5a6;">
          La función calcula todo, pero los resultados se pierden en el aire.
        </td>
      </tr>
      <tr style="border-bottom: 1px solid #333;">
        <td style="padding: 15px 20px; border-bottom: 1px solid #333; font-weight: bold; color: #74c69d;">Llamar y guardar caja</td>
        <td style="padding: 15px 20px; border-bottom: 1px solid #333;">
          <code style="background: #2d2d2d; padding: 4px 8px; border-radius: 4px; color: #d8f3dc; font-size: 0.9em;">resultado = calcular_metricas(...)</code>
        </td>
        <td style="padding: 15px 20px; border-bottom: 1px solid #333; line-height: 1.6;">
          <strong>resultado</strong> es una tupla que contiene los valores juntos: <span style="color: #b7e4c7;">(345, 86.25, 92)</span>.
        </td>
      </tr>
      <tr>
        <td style="padding: 15px 20px; font-weight: bold; color: #74c69d;">Llamar y repartir</td>
        <td style="padding: 15px 20px;">
          <code style="background: #2d2d2d; padding: 4px 8px; border-radius: 4px; color: #d8f3dc; font-size: 0.9em;">total, media, alto = calcular_metricas(...)</code>
        </td>
        <td style="padding: 15px 20px; line-height: 1.6;">
          Tienes <strong>tres variables independientes</strong> con sus valores listos para usar de forma individual.
        </td>
      </tr>
    </tbody>
  </table>
</div>

<br>

#### **Otras formas de hacerlo**

Si bien las tuplas son el estándar por ser ligeras, también podrías usar un diccionario si quieres que los valores tengan un nombre explícito:

```python

def obtener_usuario():
    return {
        "id": 101,
        "nombre": "Ana",
        "rol": "Admin"
    }

usuario = obtener_usuario()
print(usuario["nombre"]) # Imprime: Ana

```
---
<br>

#### **Salida anticipada de una función**

`return` se puede utilizar para salir anticipadamente de una función en cualquier punto. A esto se le denomina `early return`.

Esto puede ser útil para verificar condiciones y retornar un valor sin ejecutar el resto del código de la función. Bien usado, puede mejorar la legibilidad del código.

<br>

```python
def verificar_numero_negativo(numero):
    if numero < 0:
        return "El número es negativo"
    else:
        return "El número es positivo o cero"

# Llamada a la función con diferentes valores
print(verificar_numero_negativo(-5))  # Salida: El número es negativo
print(verificar_numero_negativo(10))  # Salida: El número es positivo o cero
```

<br>

## **5. Buenas Prácticas y Estilo (PEP 8) 📏**

<br>

El estándar `PEP 8` dicta cómo organizar visualmente nuestras funciones para que el código sea profesional:

**Nivel superior:** Usar dos líneas en blanco antes y después de definir una función o clase.

<br>

```python
#linea1
#linea 2
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area
#linea1
#linea 2
```

<br> 

**Dentro de clases:** Usar una línea en blanco para separar los métodos.

<br>

```python
#linea1
#linea 2
class MiClase:
    def metodo1(self):
        # Código del método 1

    def metodo2(self):
        # Código del método 2
#linea1
#linea 2
```

<br>    

**Secciones lógicas:** Se pueden usar líneas en blanco dentro de una función para separar pasos complejos.

```python
#linea1
#linea 2
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
#linea1
#linea 2
```