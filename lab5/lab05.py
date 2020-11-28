# List daftar_keranjang untuk menyimpan semua keranjang
daftar_keranjang = []

def beli_keranjang(nama_keranjang: str, kapasitas_keranjang: str):
    ''' Menambahkan keranjang baru ke daftar_keranjang

        [ARGUMENTS]
        - nama_keranjang: str
        - kapasitas_keranjang: str -> int

        [DESCRIPTION]
        Fungsi ini akan mengambil argumen dari input user dan mengubahnya menjadi list yang terdiri atas
        nama_keranjang dan representasi integer dari kapasitas_keranjang yang kemudian di tambahkan
        ke daftar_keranjang. Terakhir, fungsi ini akan memberikan feedback kepada user bahwa fungsi
        telah berhasil dieksekusi (menggunakan fstring).

    '''
    daftar_keranjang.append([nama_keranjang, int(kapasitas_keranjang)])  # Append list keranjang ke daftar_keranjang
    print(f'Berhasil menambahkan {nama_keranjang} dengan kapasitas {kapasitas_keranjang}\n')

def jual_keranjang(indeks: str):
    ''' Menjual (remove) keranjang yang dipilih dari daftar_keranjang
        
        [ARGUMENTS]
        - indeks: str

        [DESCRIPTION]
        Fungsi ini mengambil argumen command dari input user dan menggunakannya sebagai index. Index ini kemudian
        akan digunakan untuk menghapus keranjang dengan index terpilih dari daftar_keranjang dengan menggunakan method
        pop. Method pop digunakan untuk memberi feedback kepada user bahwa fungsi hapus telah berhasil di console
        (menggunakan fstring).

    '''
    terjual = daftar_keranjang.pop(int(indeks))  # Gunakan pop untuk remove dari list dan mereturn ke variabel "terjual"
    print(f'Berhasil menjual {terjual[0]} dengan kapasitas {terjual[1]}\n')

def ubah_kapasitas(indeks: str, kapasitas_baru: str):
    ''' Mengubah kapasitas keranjang yang dipilih oleh user

        [ARGUMENTS]
        - indeks: str
        - kapasitas_baru: str

        [DESCRIPTION]
        Fungsi ini mengambil argumen "indeks" dan "kapasitas_baru" dari input user dan menggunakannya sebagai parameter.
        Kedua parameter tersebut kemudian akan digunakan untuk mengubah kapasitas dari keranjang yang dipilih (pemilihan
        berdasarkan indeks dari input). Terakhir, program akan memberi feedback ke user bahwa fungsi tersebut telah berhasil
        dieksekusi (menggunakan fstring).

    '''
    daftar_keranjang[int(indeks)][1] = int(kapasitas_baru)  # Mengubah kapasitas keranjang dengan mengakses index 1 dari keranjang terpilih
    print(f'Berhasil mengubah kapasitas {daftar_keranjang[int(indeks)][0]} menjadi {kapasitas_baru}\n')

def ubah_nama(indeks: str, nama_baru: str):
    ''' Mengubah nama keranjang yang dipilih oleh user
        [ARGUMENTS]
        - indeks: str
        - nama_baru: str

        [DESCRIPTION]
        Fungsi ini mengambil argumen "indeks" dan "nama_baru" dari input user dan menggunakannya sebagai parameter.
        Kedua parameter tersebut akan digunakan untuk mengubah nama dari keranjang yang dipilih (menggunakan param indeks).
        Terakhir, program akan memberikan feedback ke user bahwa fungsi tersebut telah berhasil dieksekusi (menggunakan fstring)
    
    '''
    nama_lama = daftar_keranjang[int(indeks)][0]  # Simpan nama lama untuk di print di console
    daftar_keranjang[int(indeks)][0] = nama_baru
    print(f'Berhasil mengubah kapasitas {nama_lama} menjadi {nama_baru}\n')

def lihat(indeks: str):
    ''' Fungsi ini menampilkan informasi dari keranjang yang dipilih oleh user

        [ARGUMENTS]
        - indeks: str

        [DESCRIPTION]
        Fungsi ini mengambil argumen "indeks" dari input user dan menggunakannya sebagai parameter. Argumen tersebut
        kemudian akan digunakan untuk menampilkan informasi (nama dan kapasitas) dari keranjang yang dipilih (menggunakan parameter 
        indeks) di console (formatting menggunakan fstring)
        
    '''
    print(f'Keranjang {daftar_keranjang[int(indeks)][0]} memiliki kapasitas sebesar {daftar_keranjang[int(indeks)][1]}\n')

def lihat_semua():
    ''' Fungsi ini menampilkan semua informasi dari keranjang yang telah dimasukkan ke dalam daftar_keranjang

        [ARGUMENTS]
        - None (fungsi ini merupakan void function yang tidak mengambil argumen apapun)

        [DESCRIPTION]
        Fungsi ini mengambil semua keranjang yang ada di daftar_keranjang dan menyajikannya dalam sebuah tabel yang di print
        ke console (menggunakan formatting fstring dan padding statement).

    '''
    print('Keranjang Dek Depe')
    print('-' * 36)
    for item in daftar_keranjang:
        print(f'{item[0]:<20} | {item[1]:<10}\n')  # Formatting menggunakan padding statement dan fstring.

def total_kapasitas():
    ''' Fungsi ini menampilkan total kapasitas akumulatif yang dimiliki oleh Dek Depe
    
        [ARGUMENTS]
        - None (fungsi ini merupakan void function yang tidak mengambil argumen apapun)

        [DESCRIPTION]
        Fungsi ini mengembalikan kapasitas total dari semua keranjang yang dimiliki oleh Dek Depe (implementasi menggunakan for loop)

    '''
    capacity_sum = 0
    for lst in daftar_keranjang:
        capacity_sum += lst[1]
    print(f'Total kapasitas keranjang Dek Depe adalah {capacity_sum}\n')
    return capacity_sum



jumlah_operasi = int(input("Masukkan banyak operasi: "))
for i in range(jumlah_operasi):
    operasi = input(f'Operasi {i + 1}: ')

    commands = operasi.split()
    if commands:
        if (commands[0] == 'BELI'):
            beli_keranjang(commands[1], commands[2])

        elif (commands[0] == 'JUAL'):
            jual_keranjang(commands[1])

        elif (commands[0] == 'UBAH_KAPASITAS'):
            ubah_kapasitas(commands[1], commands[2])
        
        elif (commands[0] == 'UBAH_NAMA'):
            ubah_nama(commands[1], commands[2])

        elif (commands[0] == 'LIHAT'):
            lihat(commands[1])

        elif (commands[0] == 'LIHAT_SEMUA'):
            lihat_semua()

        elif (commands[0] == 'TOTAL_KAPASITAS'):
            total_kapasitas()
        else:
            print('Operasi tidak ditemukan! Masukkan operasi yang tepat!\n')

    else:
        print('Operasi tidak ditemukan! Masukkan operasi yang tepat!\n')