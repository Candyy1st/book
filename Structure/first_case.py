n = int(input('Masukkan Jumlah Segitiga : '))
alas = int(input('Masukkan Alas Segitiga : '))
tinggi = int(input('Masukkan Tinggi Segitiga : '))

luas = alas * tinggi / 2
luasTotal = n * luas
print(f'Luas Total : {luasTotal} satuan luas')