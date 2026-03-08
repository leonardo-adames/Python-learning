<div align="center">
    <kbd>
        <h1><b>CURSO DE PYTHON DESDE CERO</b><br></b></h1>
        <img width="2064" height="100%" alt="Image" src="../../../../notes/resources/INTRO/Py_welcome.png" altº="Image" width="100%"/>
    </kbd>
    <br>
    <br>
    <h2>FUNCIONES <kbd>def</kbd><br>EJERCICIO FINAL DE LA SECCIÓN</h2>
</div>

<br>

## Reto de Programación: Sistema de Pedidos "Pizza Dinámica" 🍕

<br>

### Contexto del Problema

Una pizzería artesanal necesita automatizar su sistema de cobros. El sistema actual falla constantemente porque no puede manejar pedidos personalizados donde los clientes agregan una cantidad impredecible de ingredientes extra o solicitan configuraciones especiales de masa.

### El Objetivo

Desarrollar una función en Python llamada `procesar_pedido_pizza` que utilice argumentos de longitud variable para procesar pedidos complejos de forma dinámica y eficiente.

### Ejemplo de Caso de Prueba

> **Entrada:** Un cliente con **$50.00** de saldo pide una **"Veggie Lover"** de **$15.00**. Agrega como extras: **"Pepperoni"** y **"Queso Cheddar"**. Además, solicita **masa="Big New York"**.
>
> **Resultado esperado:** El sistema debe calcular un total de **$23.75** ($15 base + $5 extras + $3.75 masa) y devolver un saldo restante de **$26.25**.


---

<br>

## Requerimientos Técnicos

<br>

1. **Parámetros Obligatorios (Posicionales):**
   - `nombre_pizza`: La especialidad elegida (ej. "Veggie Lover").
   - `precio_base`: El costo inicial de la pizza.
   - `saldo_cliente`: El dinero total con el que cuenta el cliente.

2. **Argumentos Posicionales Variables (`*args`):**
   - Se deben recibir todos los **ingredientes extra** que el cliente desee agregar.
   - Cada ingrediente extra tiene un costo adicional de **$2.50**.

3. **Argumentos Clave-Valor Variables (`**kwargs`):\*\*
   - La función debe capturar detalles adicionales del pedido (ej. tipo de masa, método de entrega, notas especiales).
   - **Lógica de la Masa:** Si se especifica la clave `masa="Big New York"`, se debe sumar un cargo extra de **$3.75** al total.

<br>

---

## Lógica de Negocio a Implementar

<br>

- **Cálculo del Total:** Sumar el `precio_base` + el costo total de los `*args` + los recargos encontrados en `**kwargs`.
- **Validación de Fondos:** \* Si el cliente tiene suficiente saldo, restar el total y mostrar el saldo restante.
  - Si el saldo es insuficiente, cancelar la transacción e informar al usuario.
- **Salida por Consola:** Generar un recibo detallado que desglose el precio base, los extras, el tipo de masa utilizado y el estado final del pago.

<br>

---


