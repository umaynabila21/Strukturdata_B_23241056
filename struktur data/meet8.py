# perbandingan lanjutan

#+++++3--------9++++++++
MasukkanUser = float(input("masukkan bilangan  \nkurang dari 3 atau \nlebih dari 9 :"))

# ----cek kurang dari 3
kurDar = (MasukkanUser < 3)

# ----cek kurang dari 9
lebDar = (MasukkanUser < 9)

print("lebih dari 9 = ", lebDar)

betul = kurDar or lebDar
print ("pengecekan final :", betul )



# 4 14
MasukkanUser = float(input("masukan bilngan antara 4 dan 14:"))

# versi 1
hasil = ( 4 < MasukkanUser < 14)
print(hasil)

# versi 2
lebDar = (MasukkanUser > 4 )
kurDar = (MasukkanUser < 14)
hasil2 = (lebDar and kurDar)
print (hasil)




