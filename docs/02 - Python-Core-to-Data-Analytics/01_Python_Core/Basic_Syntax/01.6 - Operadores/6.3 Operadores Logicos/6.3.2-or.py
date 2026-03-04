# Operadores lógicos OR

a = 1 == 1 or 1 < 0                           # True
b = 2 >= 2 or 1 > 0 or 45 > 90               # False
c = 56 <= 23 or 1 > 0 or 45 > 90              # True
d = 23 > 2 or 1 > 0 or 45 > 90 or 45 > 78     # True
e = 1 > 2 or 1 < 0 or 45 > 90 or 45 > 78      # False

print("1 == 1 or 1 < 0 =",a)
print("2 2 >= 2 or 1 > 0 or 45 > 90 =",b)
print("56 <= 23 or 1 > 0 or 45 > 90  =",c)
print("23 > 2 or 1 > 0 or 45 > 90 or 45 > 78 =",d)
print("1 > 2 or 1 < 0 or 45 > 90 or 45 > 78 =",e)
print()