nama = ['a', 'z', 'z', 'a', 'm']
cari = 'a'
posisi = -1

for i in range(len(nama)):
    if nama[i] == cari:
        posisi = i
        break

if posisi != -1:
    print("Huruf 'a' pertama ditemukan pada index ke-", posisi)
else:
    print("Huruf tidak ditemukan")
