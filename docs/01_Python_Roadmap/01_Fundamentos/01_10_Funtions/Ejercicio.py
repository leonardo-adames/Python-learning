def procesar_pedido_pizza(nombre_pizza, precio_base, saldo_cliente, *ingredientes_extra, **detalles_pedido):
    """
    Calcula el costo total de una pizza personalizada y el saldo restante del cliente.
    
    Parámetros:
    - nombre_pizza (str): Nombre de la especialidad (ej. 'Veggie Lover').
    - precio_base (float): Precio inicial de la pizza elegida.
    - saldo_cliente (float): Dinero disponible del cliente.
    - *ingredientes_extra: Argumentos posicionales variables para los extras (pepperoni, queso, etc.).
    - **detalles_pedido: Argumentos clave-valor para personalización (tipo_masa, tamaño, etc.).
    """

    # --- Bloque 1: Configuración de costos adicionales ---
    """
    Definimos los costos fijos para los elementos variables.
    Cada ingrediente en *args tendrá un costo, y ciertos valores en **kwargs
    como la masa 'Big New York' también pueden sumar al total.
    """
    COSTO_POR_EXTRA = 2.50
    COSTO_MASA_ESPECIAL = 3.75
    total_acumulado = precio_base

    # --- Bloque 2: Procesamiento de *args (Ingredientes Extra) ---
    """
    Iteramos sobre la tupla 'ingredientes_extra' (*args).
    Si el cliente pidió extras, se suman al total y se listan para el recibo.
    """
    conteo_extras = len(ingredientes_extra)
    costo_total_extras = conteo_extras * COSTO_POR_EXTRA
    total_acumulado += costo_total_extras

    # --- Bloque 3: Procesamiento de **kwargs (Detalles y Masa) ---
    """
    Buscamos dentro del diccionario 'detalles_pedido' (**kwargs) 
    específicamente la clave 'masa'. Si es 'Big New York', aplicamos el cargo extra.
    """
    tipo_masa = detalles_pedido.get("masa", "Tradicional")
    if tipo_masa == "Big New York":
        total_acumulado += COSTO_MASA_ESPECIAL

    # --- Bloque 4: Verificación de fondos y Saldo ---
    """
    Comparamos el total acumulado con el saldo disponible.
    Se calcula la diferencia para informar al cliente cuánto le queda.
    """
    if saldo_cliente >= total_acumulado:
        saldo_restante = saldo_cliente - total_acumulado
        estado_pago = "Pedido Procesado"
    else:
        saldo_restante = saldo_cliente  # No se pudo realizar la compra
        estado_pago = "Fondos Insuficientes"

    # --- Bloque 5: Resumen Final ---
    """
    Construimos el reporte detallado que se mostrará en pantalla.
    """
    print(f"--- RESUMEN DE COMPRA: {estado_pago} ---")
    print(f"Pizza: {nombre_pizza} (Masa: {tipo_masa})")
    print(f"Precio Base: ${precio_base:.2f}")
    
    if ingredientes_extra:
        print(f"Extras añadidos ({conteo_extras}): {', '.join(ingredientes_extra)} (+${costo_total_extras:.2f})")
    
    if tipo_masa == "Big New York":
        print(f"Cargo por masa especial: +${COSTO_MASA_ESPECIAL:.2f}")

    print(f"TOTAL FINAL: ${total_acumulado:.2f}")
    print(f"Saldo restante en su cuenta: ${saldo_restante:.2f}")
    print("-" * 40)

# --- EJEMPLO DE USO PARA EL VIDEO ---
# Pizza Veggie Lover con extras y masa Big New York
procesar_pedido_pizza(
    "Veggie Lover",           # Posicional fijo
    15.00,                    # Posicional fijo
    50.00,                    # Posicional fijo
    "Pepperoni", "Queso Cheddar", "Maíz",  # *args (pueden ser 0 o muchos)
    masa="Big New York",      # **kwargs
    entrega="Inmediata"       # **kwargs adicional
)