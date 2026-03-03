#🧩 Ejercicio: Evaluación académica con condicionales anidadas

## 🎯 Objetivo

Practicar condicionales anidadas (if dentro de otro if), operadores de comparación y type casting.

###📌 Enunciado

**Solicita al usuario:**

Su nota final (número del 0 al 100).<br>
Su porcentaje de asistencia (número del 0 al 100).<br>
Convierte ambos valores a int.

**Aplica la siguiente lógica usando condicionales anidadas:**

**Reglas de evaluación**

**Si la nota es mayor o igual a 70:**

Si la asistencia es mayor o igual a 80 → "Aprobado"<br>
Si la asistencia es menor a 80 → "Reprobado por asistencia"

**Si la nota es menor a 70:**

"Reprobado por nota"<br>
Muestra el resultado final en pantalla.

## 📋 Ejemplo de ejecución (referencial)

```python
Ingrese la nota final: 75
Ingrese la asistencia (%): 85
Resultado: Aprobado

```

```python
Ingrese la nota final: 75
Ingrese la asistencia (%): 60
Resultado: Reprobado por asistencia
```

```python
Ingrese la nota final: 60
Ingrese la asistencia (%): 90
Resultado: Reprobado por nota
```

## ⚠️ Restricciones obligatorias

**Debe usarse:**

if dentro de otro if

else

int()

**❌ No usar:**

funciones definidas por el usuario

bucles

librerías externas

## 🧠 Conceptos que se practican

Condicionales anidadas

Operadores relacionales (>=, <)

Entrada de datos con input()

Conversión de tipos (type casting)
