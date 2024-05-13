# Tabel kebenaran (logika bolean)
# not and or xor

# NOT
print("Logika NOT")
x = False
y = not x
print('value x =', x)
print('*NOT')
print('value y =', y)

# OR (semua bernilai true asalkan ada true-nya)
# berlaku untuk wanita
print("Logika OR")
x = False
y = False
z = x or y
print(x, 'OR', y, '=', z)
x = False
y = True
z = x or y
print(x, 'OR', y, '=', z)
x = True
y = False
z = x or y
print(x, 'OR', y, '=', z)
x = True
y = True
z = x or y
print(x, 'OR', y, '=', z)

# AND (hanya bernilai true, ketika keduanya true)
# berlaku untuk lelaki
print("Logika AND")
x = False
y = False
z = x and y
print(x, 'and', y, '=', z)
x = False
y = True
z = x and y
print(x, 'and', y, '=', z)
x = True
y = False
z = x and y
print(x, 'and', y, '=', z)
x = True
y = True
z = x and y
print(x, 'and', y, '=', z)

# XOR (jika keduanya sama, hasilnya false, sisanya bernilai true)
print("-----Logika XOR-----")
x = False
y = False
z = x ^ y
print(x, 'XOR', y, '=', z)
x = False
y = True
z = x ^ y
print(x, 'XOR', y, '=', z)
x = True
y = False
z = x ^ y
print(x, 'XOR', y, '=', z)
x = True
y = True
z = x ^ y
print(x, 'XOR', y, '=', z)
