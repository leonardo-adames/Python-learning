# BootCamp Python Sesión 9 - Sentencia De Coincidencia

# 9.9 Sentencia De Coincidencia // `Condición Match Case` en python // Practica.

# La sentencia de coincidencia de Python
#Ejercisio de simulación de un Operador Telefónico
print("GRACIAS PRO SU LLAMADA MENÚ DE OPCIONES")
print("\n")
print("[1] Consultas Generales")
print("[2] Solicitudas")
print("[3] Reclamos")
print("[4] Soporte Técnico")
print("[5] Reportes")
Opcion = int(input("Por Favor, Seleccione Una Opción: "))

match Opcion:
    case 1:
        print("Bienvenidos al Dpto. Consultas Generales")
    case 2:
        print("Bienvenidos al Dpto. Solicitudes")
    case 3:
        print("Bienvenidos al Dpto. Reclamos")
    case 4:
        print("Bienvenidos al Dpto. Soporte Técnico")
    case 5:
        print("Bienvenidos al Dpto. Reportes")
    case _:
        print("Opción Inexistente, Intente De Nuevamente")