# perbandingan
# lebih besar >
# lebih kecil <
# lebih besar sama dengan >=
# lebih kecil sama dengan <=
# sama dengan ==
# tidak sama dengan !=
# sama "is"
# tidak sama "is not"

x = 4
y = 5

# lebih besar >
hasil = x > y
print(x, '>', y, 'adalah', hasil)

# lebih kecil <
hasil = x < y
print(x, '<', y,'adalah', hasil )

# lebih besar sama dengan >=
hasil = x >= 2
print(x, '>=', 2, 'adalah', hasil)
hasil = x >= 4 
print(x, '>=', 4, 'adalah', hasil)

# lebih kecil sama dengan >=
hasil = x <=2
print(x, '<=', 2, 'adalah', hasil)
hasil = x <= 4
print(x, '<=', 4, 'adalah', hasil)
hasil = x <= y
print(x, '<=', y, 'adalah', hasil)

# sama dengan
hasil = x == 4
print(x, '==', 7, 'adalah', hasil)

# tidak sama dengan
hasil = x != 7
print(x, '!=' , 7, 'adalah', hasil)


# < >= <= == != ini adalah perbandingan Literal
# = 4, 4 = literal (tidak memakan memory)
# = object (memory)
#
# = 4 (bisa)
# is 4 (tidak bisa, karena yang dibandinggkan adalah literal)
# is y (bisa, karena yg dibandingkan adalah object)

# is dan isnot
hasil = x is 4
print(x, 'is', y, 'adalah', hasil)

hasil = x is not 4
print(x, 'is-not', 4, 'adalah', hasil)