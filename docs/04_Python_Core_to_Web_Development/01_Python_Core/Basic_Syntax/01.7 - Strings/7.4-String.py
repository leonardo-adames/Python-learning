# EXCERCICE 01

#PIDE AL USUARIO UNA FRASE CON ESPACIOS AL INICIO Y AL FINAL
frase = "     Leonardo Adames     "
print("Antes de usar .strip()")
print(frase)
print("\n")

# QUITA LOS ESPACIOS AL INICIO Y AL FINAL
frase_limpia = frase.strip()
print("Despues de usar .strip()")
print(frase_limpia)
print("\n")

# MOSTRAR FRASES EN MAYUSCULAS Y MINUSCULAS
print("Frase Mayuscula: " + frase_limpia.upper())
print("\n")
print("Frase Minuscula: " + frase_limpia.lower())