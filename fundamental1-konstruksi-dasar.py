# Konstruksi dasar Python
# Sequential: eksekusi berurutan
print('Halo dunia')
print('by Dodi')
print('Tanggal 13 Oktober 2022')
print('*' * 10)

# Percabangan : eksekusi terpilih
ingin_cepat = False
if ingin_cepat:
    print('jalan lurus aja ya!')
else:
    print('Jalan lain')

# Perulangan
jumlah_anak=4

for index_anak in range(1, jumlah_anak+1): #jumlah perulangan = 5 - 1 = 4
    print(f'Halo anak ke #{index_anak}')

