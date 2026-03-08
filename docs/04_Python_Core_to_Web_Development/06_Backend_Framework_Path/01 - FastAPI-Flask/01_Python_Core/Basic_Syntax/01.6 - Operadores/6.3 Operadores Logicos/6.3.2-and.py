# Operadores lógicos AND

a = 1 == 1 and 1 > 0                                # True
b = 1 < 2 and 1 > 0 and 45 <= 90                   # True
c = 1 >= 2 and 1 > 0 and 45 > 90                   # False
d = 1 <= 2 and 1 > 0 and 45 <= 90 and 45 <= 78      # True
e = 1 > 2 and 1 > 0 and 45 > 90 and 45 >= 78      # False

print("1 == 1 and 1 > 0 =",a)
print("1 < 2 and 1 > 0 and 45 <= 90 =",b)
print("1 >= 2 and 1 > 0 and 45 > 90 =",c)
print("1 <= 2 and 1 > 0 and 45 <= 90 and 45 <= 78 =",d)
print("1 > 2 and 1 > 0 and 45 > 90 and 45 >= 78 =",e)
print()