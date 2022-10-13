"""""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""""

kamus_ind_eng = {'Istri': 'Wife', 'Anak': 'Son', 'Ayah': 'Father', 'Ibu': 'Mother' }

print(kamus_ind_eng)
print(kamus_ind_eng['Istri'])
print(kamus_ind_eng['Ibu'])

print('\nData ini dikirimkan oleh Server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal' : '13-10-2022',
    'driver_list': [
        {'nama': 'Dodi', 'Jarak': 10},
        {'nama': 'Samsul', 'Jarak': 30},
        {'nama': 'Falah', 'Jarak': 100},
        {'nama': 'Jukifli', 'Jarak': 1000},
    ]
}
print(f"\nDriver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['Jarak']} meter")