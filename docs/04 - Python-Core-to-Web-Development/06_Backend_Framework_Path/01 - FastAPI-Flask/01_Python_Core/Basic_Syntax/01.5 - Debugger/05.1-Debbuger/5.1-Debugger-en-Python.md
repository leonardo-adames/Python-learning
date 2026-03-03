# BootCamp Python Sesión 5 - Debugger Introducción

## 4.1 Debugger (Depuración) en Python

### ¿Qué es?

En Python, un `debugger` (depurador) es una herramienta que te permite detener la ejecución de un programa en puntos específicos para inspeccionar su estado, encontrar errores y entender su comportamiento paso a paso.

### 🔍 Funciones principales de un debugger

1. *Puntos de interrupción (`breakpoints`):*

* Puedes indicar en qué línea detener la ejecución para examinar variables y flujo.

2. *Ejecución paso a paso:*

* Avanzar línea por línea para ver cómo cambian los valores.

3. *Inspección de variables:*

* Consultar el contenido de variables y estructuras de datos en tiempo real.

4. *Evaluación de expresiones:*

* Probar código directamente mientras el programa está detenido.

5.*Control del flujo:*

* Saltar funciones, retroceder en la `pila de llamadas` o continuar hasta el siguiente `breakpoint`.

### 🛠 Debugger integrado en Python

Python incluye el módulo estándar pdb (Python Debugger).

**Ejemplo básico:**

```python
import pdb

def suma(a, b):
    pdb.set_trace()  # Punto de interrupción
    return a + b

resultado = suma(5, 3)
print("Resultado:", resultado)

```

Cuando el programa llega a `pdb.set_trace()`, se detiene y te permite:

* Escribir n para ir a la siguiente línea.
* Escribir c para continuar hasta el próximo breakpoint.
* Escribir p variable para imprimir el valor de una variable.
* Escribir q para salir del depurador.

### 💡 Alternativas gráficas

* VS Code Debugger
* PyCharm Debugger
* Spyder Debugger

### Estas ofrecen una interfaz visual para manejar breakpoints y ver variables sin usar comandos de consola.
