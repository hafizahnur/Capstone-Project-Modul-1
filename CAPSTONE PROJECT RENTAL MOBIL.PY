#CAPSTONE PROJECT MODUL 1
#by NUR HAFIZAH
#PROGRAM RENTAL MOBIL


from tabulate import tabulate

List_mobil = [
    {'id' : 'XM123',
    'tipe': 'xpander',
     'tahun': 2020,
     'warna': 'hitam',
     'keterangan': 'tersedia',
     'harga': 300000},

    {'id' : 'HN456',
    'tipe': 'honda',
     'tahun': 2021,
     'warna': 'silver',
     'keterangan': 'kosong',
     'harga': 300000},

    {'id' : 'IN789',
    'tipe': 'innova',
     'tahun': 2020,
     'warna': 'putih',
     'keterangan': 'tersedia',
     'harga': 300000},
]

# Function untuk mencari mobil berdasarkan id
def cari_mobil_by_id(id_mobil):
    return [mobil for mobil in List_mobil if mobil['id'] == id_mobil]

# Function untuk menampilkan data mobil
def tampilkan(Data):
    if len(Data) > 0:
        print(tabulate(Data, headers='keys', tablefmt='grid'))
    else:
        print("Data tidak ditemukan")

# MENU MENAMPILKAN DATA
def menu_read():
    while True:
        print('''
    =====Menu Tampilkan Data=====

    1. Tampilkan semua data mobil
    2. Lihat mobil dengan nomor id
    3. Kembali ke menu utama 
    ''')
        
        opsi = input('Masukkan angka yang ingin dipilih: ')

        # Menampilkan seluruh data mobil
        if opsi == '1':
            if len(List_mobil) > 0:
                tampilkan(List_mobil)
            else:
                print('\nData Mobil Tidak Ditemukan')
                
        # Menampilkan mobil berdasarkan nomor id
        elif opsi == '2':
            if len(List_mobil) > 0:
                cari_id = input('\nMasukkan nomor id mobil: ').upper()
                mobil_ditemukan = cari_mobil_by_id(cari_id)
                tampilkan(mobil_ditemukan)
            else:
                print('\nTidak Ada Data Mobil. Mohon Tambahkan Data Mobil Terlebih Dahulu')
                
        # Kembali ke menu utama
        elif opsi == '3':
            break
        else:
            print('\nIsi Sesuai Dengan Pilihan Menu!')


#2. MENAMBAHKAN DATA MOBIL

def menu_create():
    while True:
        print('''
    =====Menu Untuk Menambahkan Data=====
                                   
    1. Menambahkan data mobil
    2. Kembali ke menu utama
    ''')

        opsi = input('Masukkan angka yang ingin dipilih: ')

        #Menambah data mobil
        if opsi == '1':
            new_id = str(input('\nMasukkan nomor id: ')).upper()
            #Data duplicate
            if any(mobil['id'] == new_id for mobil in List_mobil):
                print(f'\nNomor ID {new_id} sudah ada dalam daftar mobil')
            #Menambah data (non duplicate data)
            else:
                new_tipe = input('Masukkan tipe mobil: ')
                new_tahun = input('Masukkan informasi tahun mobil: ')
                new_warna = input('Masukkan warna mobil: ')
                new_keterangan = input ('Masukkan informasi keterangan rental: ')
                new_harga = int(input('Masukkan harga sewa mobil: '))
                #Menambahkan menu pilihan untuk menyimpan data
                print('Tekan 1 untuk menyimpan data atau tekan 2 untuk membatalkan: ')
                pilihan = int(input('opsi: '))
                if pilihan == 1:
                    List_mobil.append({
                        'id': new_id,
                        'tipe': new_tipe,
                        'tahun': int(new_tahun),
                        'warna': new_warna,
                        'harga': int(new_harga),
                        'keterangan': new_keterangan
                    })
                    tampilkan(List_mobil) 
                    print('Data berhasil disimpan')

                elif pilihan == 2:
                    print('Data tidak tersimpan')
                else:
                    print('Isi Sesuai Dengan Pilihan Menu!')
        #Kembali ke menu utama
        elif opsi == '2':
            break
        else:
            print('Isi Sesuai Dengan Pilihan Menu!')

#3. MEMPERBAHARUI DATA MOBIL

def menu_update():
    while True:
        print('''\nMenu Ini Akan Mengupdate Mobil Dengan Menggunakan Nomor ID''')
        Id_mobil = input("\nMasukkan Nomor Id: ").upper()
        
        # Mencari mobil dengan Nomor ID yang sesuai
        mobil_ditemukan = None
        for mobil in List_mobil:
            if Id_mobil == mobil['id']:
                mobil_ditemukan = mobil
                break
        else:
            print(f'\nTidak ada data mobil dengan Nomor ID {Id_mobil}')
            continue

        # Menampilkan data mobil sebelum diupdate
        tampilkan([mobil_ditemukan])

        while True:
            # Memilih menu untuk update data
            print('\nMasukkan Menu Data Yang Akan Diupdate')
            print('\nMenu 1: Update Keterangan Mobil')
            print('Menu 2: Update Harga Mobil')
            print('Menu 3: Exit')

            try:
                menu = int(input('Masukkan menu (1/2/3): '))

                if menu == 1:
                    new_keterangan = input('Masukkan keterangan mobil: ')
                    mobil_ditemukan.update({'keterangan': new_keterangan})
                    print('Data mobil telah diperbarui.')

                elif menu == 2:
                    new_harga = int(input('Masukkan harga mobil: '))
                    mobil_ditemukan.update({'harga': new_harga})
                    print('Data mobil telah diperbarui.')

                elif menu == 3:
                    print('Keluar dari menu update.')
                    break

                else:
                    print('Pilihan tidak valid. Masukkan angka 1, 2, atau 3.')

                # Menampilkan pilihan untuk menyimpan data 
                simpan = input('\nApakah Anda ingin menyimpan data? (ya/tidak): ').lower()
                if simpan == 'ya':
                    print('\nData Berhasil Disimpan')
                else:
                    print('\nData Belum Tersimpan')

            except ValueError:
                print('Masukkan angka yang valid.')

        opsi = input('''\nApakah Anda ingin memperbarui data mobil lainnya? (ya/tidak): ''').lower()
        if opsi != 'ya':
            break                                              

#4. MENGHAPUS DATA MOBIL

def menu_delete():
    while True:
        print('''\nMenu Ini Akan Menghapus Mobil Dengan Menggunakan Nomor Id''')
        Id_mobil = input('Masukkan Nomor Id: ').upper()

        # Mencari mobil dengan Nomor ID yang sesuai
        mobil_ditemukan = None
        for mobil in List_mobil:
            if Id_mobil == mobil['id']:
                mobil_ditemukan = mobil
                break
        else:
            print(f'\nTidak ada data mobil dengan Nomor ID {Id_mobil}')
            continue

        # Menampilkan data mobil sebelum dihapus
        tampilkan([mobil_ditemukan])

        opsi = input('\nApakah Anda yakin ingin menghapus data ini? (ya/tidak): ').lower()
        if opsi == 'ya':
            List_mobil.remove(mobil_ditemukan)
            print('Data mobil berhasil dihapus.')
        else:
            print('Data mobil tidak dihapus.')

        opsi_lanjut = input('\nApakah Anda ingin menghapus mobil lainnya? (ya/tidak): ').lower()
        if opsi_lanjut != 'ya':
            break

#5. EXIT

def exit_program():
    print('\nAnda Telah keluar dari Aplikasi Rental Mobil Sebong!. TERIMA KASIH!!!')
    exit()

#MENU UTAMA

while True:
    print('''
          SELAMAT DATANG DI RENTAL MOBIL SEBONG
        -----------------------------------------

        List Menu:
        1. Show Mobil
        2. Tambah Data
        3. Update Data
        4. Delete Data
        5. Exit Program
    ''')

    try:
        menu = int(input("Masukkan pilihan menu (1-5): "))

        if menu == 1:
            menu_read()  
        elif menu == 2:
            menu_create()  
        elif menu == 3:
            menu_update()  
        elif menu == 4:
            menu_delete()  
        elif menu == 5:
            exit_program()
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1-5.")

    except ValueError:
        print("Masukkan sesuai petunjuk! Pilih angka 1-5.")


        



           





 



           
            







        