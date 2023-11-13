from tabulate import tabulate
from datetime import date
import math

# Database untuk anggota gym
db_anggota = [
    {'ID': 'FPT001', 'Nama': 'Andi Susanto', 'Jenis Kelamin': 'Pria', 'Berat': 60, 'Tinggi': 175, 'Nama Pelatih': 'Joko Santoso', 'Tanggal Registrasi': '2023-01-01'},
    {'ID': 'FPT002', 'Nama': 'Rina Dewi', 'Jenis Kelamin': 'Wanita', 'Berat': 45, 'Tinggi': 160, 'Nama Pelatih': 'Rina Wijaya', 'Tanggal Registrasi': '2023-02-15'},
    {'ID': 'FPT003', 'Nama': 'Budi Pratama', 'Jenis Kelamin': 'Pria', 'Berat': 80, 'Tinggi': 180, 'Nama Pelatih': 'Fitriani', 'Tanggal Registrasi': '2023-03-20'},
    {'ID': 'FPT004', 'Nama': 'Siti Rahayu', 'Jenis Kelamin': 'Wanita', 'Berat': 80, 'Tinggi': 165, 'Nama Pelatih': 'Rina Wijaya', 'Tanggal Registrasi': '2023-04-10'},
    {'ID': 'FPT005', 'Nama': 'Eko Saputro', 'Jenis Kelamin': 'Pria', 'Berat': 95, 'Tinggi': 170, 'Nama Pelatih': 'Joko Santoso', 'Tanggal Registrasi': '2023-05-05'},
    {'ID': 'FPT006', 'Nama': 'Lina Kurnia', 'Jenis Kelamin': 'Wanita', 'Berat': 130, 'Tinggi': 162, 'Nama Pelatih': 'Rina Wijaya', 'Tanggal Registrasi': '2023-06-12'},
    {'ID': 'FPT007', 'Nama': 'Ahmad Fauzi', 'Jenis Kelamin': 'Pria', 'Berat': 68, 'Tinggi': 175, 'Nama Pelatih': 'Joko Santoso', 'Tanggal Registrasi': '2023-07-03'},
    {'ID': 'FPT008', 'Nama': 'Dewi Fitriani', 'Jenis Kelamin': 'Wanita', 'Berat': 60, 'Tinggi': 168, 'Nama Pelatih': 'Rina Wijaya', 'Tanggal Registrasi': '2023-08-28'},
    {'ID': 'FPT009', 'Nama': 'Hadi Sutanto', 'Jenis Kelamin': 'Pria', 'Berat': 75, 'Tinggi': 178, 'Nama Pelatih': 'Joko Santoso', 'Tanggal Registrasi': '2023-09-15'},
    {'ID': 'FPT010', 'Nama': 'Sari Indah', 'Jenis Kelamin': 'Wanita', 'Berat': 58, 'Tinggi': 160, 'Nama Pelatih': 'Fitriani', 'Tanggal Registrasi': '2023-10-22'},
]

db_pelatih = [
    {'ID': 'XPT001', 'Nama': 'Joko Santoso', 'Jenis Kelamin': 'Pria', 'email': 'joko.santoso@gmail.com', 'phone': '081234567890'},
    {'ID': 'XPT002', 'Nama': 'Rina Wijaya', 'Jenis Kelamin': 'Wanita', 'email': 'rina.wijaya@gmail.com', 'phone': '087654321098'},
    {'ID': 'XPT003', 'Nama': 'Fitriani', 'Jenis Kelamin': 'Wanita', 'email': 'fitriani24@gmail.com', 'phone': '081112223344'},
]

def tampilkan_menu():
    print("====== DATABASE ANGGOTA GYM ======")
    print(r"""
❚█══█❚ -+-+-+ ❚█══█❚ +-+-+- ❚█══█❚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
    print("=========== Menu Utama ===========")
    print("1. Tampilkan Data Anggota")
    print("2. Tambah Data Anggota Baru")
    print("3. Ubah Data Anggota")
    print("4. Hapus Data Anggota")
    print("5. Urutkan Data Anggota")
    print("6. Kalkulasi Indeks Massa Tubuh (IMT) Anggota")
    print("7. Tampilkan Data Pelatih")
    print("8. Keluar Program")

def tampilkan_anggota(db, nama_data):
    while True:
        print(f"\n=========== Data {nama_data} ===========")
        
        # kondisi jika database kosong
        if not db:
            print(f"Database {nama_data} kosong.")
            break

        print("1. Menampilkan semua data")
        print("2. Mencari Data berdasarkan kolom")
        print("3. Kembali ke menu utama")

        pilihan_submenu = input("Pilih submenu (1-3): ")

        if pilihan_submenu == '1':
            headers = "keys"
            print(tabulate(db, headers=headers, showindex=True, tablefmt="grid"))
        elif pilihan_submenu == '2':
            cari_anggota(db)
        elif pilihan_submenu == '3':
            break
        else:
            print("Pilihan submenu tidak valid. Silakan pilih lagi.")

def cari_anggota(db):
    headers = "keys"
    print(tabulate(db, headers=headers, showindex=True, tablefmt="grid"))
    print("\n=========== Pencarian Data Anggota ===========")
    kolom_pencarian = input("Masukkan kolom untuk pencarian (Nama, Jenis Kelamin, dll.): ")

    # kondisi jika data kolom yang di input tidak ada
    if kolom_pencarian not in db[0]:
        print(f"\nKolom \033[4m{kolom_pencarian}\033[m tidak valid. ingat \033[4mCASE-SENSITIVE\033[m\n")
        return

    nilai_pencarian = input(f"Masukkan nilai untuk kolom {kolom_pencarian} (case-sensitive): ")
    
    anggota_ditemukan = [anggota for anggota in db if anggota[kolom_pencarian] == nilai_pencarian]

    # kondisi jika data baris yang di input tidak ada
    if not anggota_ditemukan:
        print("Data tidak ditemukan.")
    else:
        headers = "keys"
        print(tabulate(anggota_ditemukan, headers=headers, showindex=True, tablefmt="grid"))

def tambah_anggota(db):
    while True:
        headers = "keys"
        print(tabulate(db, headers=headers, showindex=True, tablefmt="grid"))
        print("\n=========== Penambahan Data Anggota Baru ===========")
        print("1. Masukkan Data")
        print("2. Kembali ke menu utama")
        ta_submenu_pilihan = input("Pilih submenu (1/2): ")

        if ta_submenu_pilihan == '1':
            anggota_baru = {}

            ta_id_input = input("Masukkan ID (angka): ")
            
            if not ta_id_input.isdigit():
                print("\n\033[4mInput ID terakhir tidak valid. Harap masukkan angka saja.\033[m\n")
                continue

            # Melakukan pengecekan duplikat data dan menaruhnya di format FPT{000}
            existing_id = [member['ID'] for member in db]
            id_baru = int(ta_id_input)
            id_baru_str = str(id_baru).zfill(3)
            id_anggota_baru = f'FPT{id_baru_str}'

            if id_anggota_baru in existing_id:
                print("\n\033[4mData sudah ada.\033[m\n")
                continue

            anggota_baru['ID'] = id_anggota_baru
            
            # Memasukkan data kolom dengan kondisi
            anggota_baru['Nama'] = input("Masukkan Nama Anggota (alfabet): ")

            # Validasi nama hanya huruf saja
            if not anggota_baru['Nama'].replace(' ','').isalpha():
                print("\n\033[4mNama harus berupa huruf saja.\033[m\n")
                continue

            jenis_kelamin_input = input("Masukkan Jenis Kelamin (Pria/Wanita): ").capitalize()

            # Validasi jenis kelamin sesuai syntax
            if jenis_kelamin_input == 'P' or jenis_kelamin_input == 'Pria':
                anggota_baru['Jenis Kelamin'] = 'Pria'
            elif jenis_kelamin_input == 'W' or jenis_kelamin_input == 'Wanita':
                anggota_baru['Jenis Kelamin'] = 'Wanita'
            else:
                print("\n\033[4mJenis Kelamin tidak valid. Harap masukkan Pria/P atau Wanita/W.\033[m\n")
                continue

            anggota_baru['Berat'] = input("Masukkan Berat Badan (angka): ")
            anggota_baru['Tinggi'] = input("Masukkan Tinggi Badan (angka): ")
            
            # Validasi berat dan tinggi integer
            if not anggota_baru['Berat'].isdigit() or not anggota_baru['Tinggi'].isdigit():
                print("\n\033[4mBerat dan Tinggi harus berupa angka.\033[m\n")
                continue
            # Validasi berat dan tinggi realistis
            if not (20 <= int(anggota_baru['Berat']) <= 600) or not (50 <= int(anggota_baru['Tinggi']) <= 300):
                print("\n\033[4mBerat dan Tinggi harus berada dalam rentang realistis.\033[m\n")
                continue
            
            anggota_baru['Nama Pelatih'] = input("Masukkan Nama Pelatih (alfabet): ")
            anggota_baruC = anggota_baru['Nama Pelatih'].title()
            
            # Validasi nama pelatih yang sesuai di db_pelatih
            if anggota_baruC not in [pelatih['Nama'] for pelatih in db_pelatih]:
                print(f"\n\033[4mPelatih bernama {anggota_baruC} tidak ada. Cek Menu 7 di Menu Utama\033[m\n")
                continue
            
            anggota_baru['Tanggal Registrasi'] = date.today().strftime("%Y-%m-%d")

            # Konfirmasi penyimpanan data
            konfirmasi = input("\nApakah Anda yakin ingin menyimpan data anggota ini? (iya/tidak): ").lower()
            
            if konfirmasi == 'iya' or konfirmasi == 'y':
                db.append(anggota_baru)
                print("\n\033[4mData anggota baru berhasil ditambahkan.\033[m\n")
            else:
                print("\n\033[4mData anggota baru tidak disimpan.\033[m\n")
            break

        elif ta_submenu_pilihan == '2':
            print("\nKembali ke menu utama.\n")
            break

        else:
            print("\nMenu tidak valid. Silakan pilih lagi.\n")

def ubah_anggota(db):
    while True:
        print("\n=========== Pengubahan Data Anggota ===========")
        print("1. Ubah Data")
        print("2. Kembali ke menu utama")
        submenu_pilihan = input("Pilih submenu (1/2): ")

        if submenu_pilihan == '1':
            headers = "keys"
            print(tabulate(db, headers=headers, showindex=True, tablefmt="grid"))
            ua_id_input = input("Masukkan ID Anggota yang ingin diubah (angka saja tanpa FPT): ")

            # Validasi input berupa angka saja
            if ua_id_input.isdigit():
                id_anggota = f'FPT{int(ua_id_input):03d}'
            else:
                print("\n\033[4mInput ID tidak valid. Harap masukkan angka.\033[m\n")
                return

            for anggota in db:
                if anggota['ID'] == id_anggota:
                    
                    # untuk menampilkan tabel kolom dengan nilai yang dipilih
                    print(f"\nData Anggota yang ingin diubah:")
                    headers = [kolom for kolom in db[0].keys()]
                    data = [[kolom, anggota[kolom]] for kolom in headers]
                    print(tabulate(data, headers=['Kolom', 'Nilai'], tablefmt="grid"))
                    
                    # Memasukkan data kolom yang ingin diubah dengan kondisi
                    kolom_ubah = input("Masukkan \033[4mkolom\033[m yang ingin diubah (case-sensitive): ")

                    if kolom_ubah == 'ID':
                        print("\n\033[4mID tidak dapat diubah.\033[m\n")
                        return

                    if kolom_ubah not in db[0]:
                        print(f"\nKolom \033[4m{kolom_ubah}\033[m tidak valid. Ingat \033[4mCASE-SENSITIVE\033[m.\n")
                        return

                    if kolom_ubah in ['Nama']:
                        nilai_baru = input(f"Masukkan nilai baru untuk kolom {kolom_ubah} (alfabet): ")

                        if not nilai_baru.isalpha():
                            print(f"\n\033[4m{kolom_ubah} harus berupa huruf.\033[m\n")
                            return
                    elif kolom_ubah == 'Jenis Kelamin':
                        nilai_baru = input(f"Masukkan nilai baru untuk kolom {kolom_ubah} (Pria/Wanita): ").capitalize()

                        if nilai_baru not in ['Pria', 'Wanita']:
                            print("\n\033[4mJenis Kelamin tidak valid. Harap masukkan Pria atau Wanita.\033[m\n")
                            return
                    elif kolom_ubah in ['Berat', 'Tinggi']:
                        nilai_baru = input(f"Masukkan nilai baru untuk kolom {kolom_ubah} (angka): ")

                        if not nilai_baru.isdigit():
                            print(f"\n\033[4m{kolom_ubah} harus berupa angka.\033[m\n")
                            return
                    elif kolom_ubah in ['Nama Pelatih']:
                        existing_nama_pelatih = [pelatih['Nama'] for pelatih in db_pelatih]
                        nilai_baru = input(f"Masukkan nilai baru untuk kolom {kolom_ubah} (Cek menu 7 di menu utama): ")

                        # Validate that the entered value exists in db_pelatih
                        if nilai_baru not in existing_nama_pelatih:
                            print(f"\n\033[4mPelatih bernama {nilai_baru} tidak ada. Cek Menu 7 di Menu Utama\033[m\n")
                            return
                    elif kolom_ubah == 'Tanggal Registrasi':
                        nilai_baru = input(f"Masukkan nilai baru untuk kolom {kolom_ubah} (YYYY-MM-DD): ")

                        # Validasi format tanggal
                        if (
                            len(nilai_baru) == 10 and
                            nilai_baru[4] == '-' and
                            nilai_baru[7] == '-' and
                            nilai_baru[:4].isdigit() and
                            nilai_baru[5:7].isdigit() and
                            nilai_baru[8:].isdigit()
                        ):
                            print(f"\nTanggal Registrasi: {nilai_baru}\n")
                        else:
                            print("\n\033[4mFormat tanggal tidak valid. Harap gunakan format YYYY-MM-DD.\033[m\n")
                            continue
                    
                    else:
                        print(f"Kolom {kolom_ubah} tidak ada.")
                        continue

                    konfirmasi_ubah = input("\nApakah Anda yakin ingin menyimpan perubahan data anggota ini? (iya/tidak): ").lower()
            
                    if konfirmasi_ubah == 'iya' or konfirmasi_ubah == 'y':
                        anggota[kolom_ubah] = nilai_baru
                        print("Data anggota berhasil diubah.")
                    else:
                        print("\n\033[4mPerubahan data anggota tidak disimpan.\033[m\n")
                    break
            else:
                print("Data anggota tidak ditemukan.")
            break

        elif submenu_pilihan == '2':
            print("\nKembali ke menu utama.\n")
            break

        else:
            print("\nMenu tidak valid. Silakan pilih lagi.\n")


def hapus_anggota(db):
    while True:
        print("\n=========== Penghapusan Data Anggota ===========")
        print("1. Hapus Data")
        print("2. Kembali ke menu utama")
        ha_submenu_pilihan = input("Pilih submenu (1/2): ")

        if ha_submenu_pilihan == '1':
            headers = "keys"
            print(tabulate(db, headers=headers, showindex=True, tablefmt="grid"))
            ha_id_input = input("Masukkan ID Anggota yang ingin dihapus (angka): ")

            # melakukan pengecekan apakah data yg di input ada
            if ha_id_input.isdigit():
                id_anggota = f'FPT{int(ha_id_input):03d}'
            else:
                print("\n\033[4mInput ID tidak valid. Harap masukkan angka.\033[m\n")
                return

            found = False
            for anggota in db:
                if anggota['ID'] == id_anggota:
                    db.remove(anggota)
                    print(f"Data anggota berhasil dihapus:\n\n\033[4m{anggota}\033[m\n")
                    found = True
                    break

            if not found:
                print("\n\033[4mData anggota tidak ditemukan.\033[m\n")
            
            break

        elif ha_submenu_pilihan == '2':
            print("\nKembali ke menu utama.\n")
            break

        else:
            print("\nMenu tidak valid. Silakan pilih lagi.\n")

def urutkan_anggota(db):
    while True:
        headers = "keys"
        print(tabulate(db, headers=headers, showindex=True, tablefmt="grid"))
        print("\n=========== Pengurutan Data Anggota ===========")
        print("1. Nama (A-Z)")
        print("2. Nama (Z-A)")
        print("3. Berat (rendah-tinggi)")
        print("4. Berat (tinggi-rendah)")
        print("5. Tinggi (rendah-tinggi)")
        print("6. Tinggi (tinggi-rendah)")
        print("7. Tanggal registrasi (terbaru-terlama)")
        print("8. Tanggal registrasi (terlama-terbaru)")
        print("9. Kembali ke menu utama")
        opsi_urut = input("Pilih opsi pengurutan (1-9): ")

        if opsi_urut == '9':
            print("\nKembali ke menu utama.\n")
            break

        if opsi_urut not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("\nOpsi tidak valid. Silakan pilih lagi.\n")
            continue

        reverse_order = False
        if opsi_urut in ['2', '4', '6', '8']:
            reverse_order = True

        # Melakukan sorting berdasarkan key
        if opsi_urut == '1' or opsi_urut == '2':
            temp = lambda x: x['Nama']
        elif opsi_urut == '3' or opsi_urut == '4':
            temp = lambda x: x['Berat']
        elif opsi_urut == '5' or opsi_urut == '6':
            temp = lambda x: x['Tinggi']
        elif opsi_urut == '7' or opsi_urut == '8':
            temp = lambda x: x['Tanggal Registrasi']

        db_sorted = sorted(db, key=temp, reverse=reverse_order)
        headers = "keys"
        print(tabulate(db_sorted, headers=headers, showindex=True, tablefmt="grid"))
        print("\n\033[4mData anggota berhasil diurutkan.\033[m\n")
        break

def kalkulasi_imt(db):
    while True:
        print("\n=========== Kalkulasi Indeks Massa Tubuh (IMT) ===========")
        print("1. Masukkan ID Anggota")
        print("2. Kembali ke menu utama")
        imt_submenu_pilihan = input("Pilih submenu (1/2): ")

        if imt_submenu_pilihan == '1':
            headers = "keys"
            print(tabulate(db, headers=headers, showindex=True, tablefmt="grid"))
            imt_id_input = input("Masukkan ID Anggota (angka saja tanpa FPT): ")

            if imt_id_input.isdigit():
                id_anggota = f'FPT{int(imt_id_input):03d}'
            else:
                print("\n\033[4mInput ID tidak valid. Harap masukkan angka.\033[m\n")
                continue

            found = False
            for anggota in db:
                if anggota['ID'] == id_anggota:
                    nama_user = anggota['Nama']
                    massa = anggota['Berat']
                    tinggi = anggota['Tinggi']

                    tinggi_meter = tinggi / 100
                    imt = massa / math.pow(tinggi_meter, 2)

                    print(f"\n\033[4m{nama_user}\033[m memiliki Massa \033[4m{massa}\033[m kg dan tinggi \033[4m{tinggi_meter}\033[m m")

                    if imt < 18.5:
                        print(f"\nIMT \033[4m{round(imt, 2)}\033[m, berat badan \033[4mkurang\033[m\n")
                    elif 18.5 <= imt <= 24.9:
                        print(f"\nIMT \033[4m{round(imt, 2)}\033[m, berat badan \033[4mideal!\033[m\n")
                    elif 25 <= imt <= 29.9:
                        print(f"\nIMT \033[4m{round(imt, 2)}\033[m, berat badan \033[4mberlebih\033[m\n")
                    elif 30 <= imt <= 39.9:
                        print(f"\nIMT \033[4m{round(imt, 2)}\033[m, berat badan \033[4msangat berlebih\033[m\n")
                    else:
                        print(f"\nIMT \033[4m{round(imt, 2)}\033[m, berat badan \033[4mobesitas\033[m\n")

                    found = True
                    break

            if not found:
                print("\n\033[4mData anggota tidak ditemukan.\033[m\n")
            break

        elif imt_submenu_pilihan == '2':
            print("\nKembali ke menu utama.\n")
            break

        else:
            print("\nMenu tidak valid. Silakan pilih lagi.\n")

def cek_admin():
    print(r'''
=================================================================================================
          
 ██████╗██╗   ██╗███╗   ███╗    ██████╗  █████╗ ████████╗ █████╗ ██████╗  █████╗ ███████╗███████╗
██╔════╝╚██╗ ██╔╝████╗ ████║    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
██║  ███╗╚████╔╝ ██╔████╔██║    ██║  ██║███████║   ██║   ███████║██████╔╝███████║███████╗█████╗  
██║   ██║ ╚██╔╝  ██║╚██╔╝██║    ██║  ██║██╔══██║   ██║   ██╔══██║██╔══██╗██╔══██║╚════██║██╔══╝  
╚██████╔╝  ██║   ██║ ╚═╝ ██║    ██████╔╝██║  ██║   ██║   ██║  ██║██████╔╝██║  ██║███████║███████╗
 ╚═════╝   ╚═╝   ╚═╝     ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
          
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢤⡖⠺⠉⠓⠢⣄⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⢞⣿⣿⣭⣟⣯⣾⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⢸⣅⠉⠀⢻⣦⠀⡀⠘⣆⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣟⣿⡿⣿⣿⣿⢟⣿⣿⠟⢿⡀⠀⠀⠀⠀⠀⠀⠀⢟⣿⣾⣿⣿⣿⣇⠀⢡⠘⣆⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣶⣿⣻⡿⠁⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠉⠉⠁⢻⠈⡆⢳⡈⢳⡀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣽⣿⡏⠀⠐⠾⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠟⢰⡥⠀⢝⣄⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣷⡘⠃⠀⠀⠀⠀⠙⢁⣱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⢣⠞⣀⢇⠈⠱⠚⣆⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⢿⣻⣿⣿⣿⡅⠀⠀⠀⢦⣬⡇⠀⠀⠀⠀⠀⠀⠀⢠⠚⡏⠉⠑⢺⡄⠀⠀⠙⣧⡀⠇⠀⡇
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⣷⠈⠉⠙⠛⠿⢿⣷⣦⣄⢰⣾⠖⣊⣉⡩⠍⢉⠓⠶⣿⢁⠜⢇⠁⢀⣹⣷⣤⣤⣈⣇⠀⣸⢧
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⢛⡇⠉⠀⠀⡀⢀⡀⠀⠀⠉⢙⡏⠁⠀⢹⣇⡀⠙⣏⠢⡌⡉⠉⣒⡷⠚⠉⠉⢻⣿⣿⣿⣵⣾⣷⣾
                ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠚⠁⢀⣼⠋⣿⡅⠀⠀⠀⠀⠈⠉⠓⣦⡨⠀⡀⠀⠀⢈⣉⡒⠒⣶⡶⠂⠉⠀⠠⣤⣴⣶⣾⣿⣿⠿⠛⠉⠁
                ⠀⠀⠀⠀⠀⠀⠀⣴⠋⠉⠙⠋⠉⢸⣥⡤⠜⠋⢤⣦⢤⣤⣴⡾⠟⠁⠀⠙⢒⣫⣥⣴⣶⣿⣏⠀⠉⠛⠿⢿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀
                ⠀⠀⠀⠀⢀⡤⠚⠙⣷⣿⣦⡀⠀⢨⡏⠀⠀⠀⠀⠀⠀⠀⣩⠀⠀⠀⠉⠉⠉⢉⡛⢻⣿⣿⣿⣷⣶⣶⣶⣶⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⣰⠏⢀⠀⠀⣖⠈⠁⠉⠙⢻⣷⣄⣀⣤⣤⡴⠿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⡏⢰⡟⠀⠀⣿⡄⠀⠀⠀⣿⠀⠀⠀⠀⠀⢀⣴⠟⠁⢿⣄⣀⡀⠀⣀⣤⣶⣿⣿⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⣸⠀⢸⡁⠀⠀⠸⣿⣄⠀⡀⣿⠀⠀⡠⣶⡷⠋⡀⠀⠀⠚⠛⠛⠛⠛⠛⠛⠃⠈⠑⡿⢸⣯⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⢠⠇⠀⠘⣿⣦⣤⣤⣿⡟⠛⠓⢿⣞⠻⠟⣔⠲⡇⣀⡀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⢠⣾⣺⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⢸⠀⠀⠀⣿⣿⠉⠛⠿⢦⣄⡠⠘⡆⣀⣤⠀⠀⠀⢐⣮⠗⠃⠋⠛⠛⠛⠛⠛⢻⣿⡿⡍⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⣼⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠭⠌⣧⢾⣧⣤⣾⣦⠥⢠⣀⣀⢄⣠⣦⣶⣾⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⣿⠀⣀⣴⣿⣿⣿⣿⣦⡂⠀⠀⠀⣾⣙⡇⠀⠀⠀⠀⠀⠀⠁⠀⣡⣿⣿⣿⣿⣯⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⣿⡿⢋⣡⣾⣿⣿⣟⣻⠿⣿⠷⣤⣿⣿⣇⠀⠀⠀⠀⠀⠠⣀⣿⣿⣿⠛⠛⠻⠏⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⢰⡟⣻⣿⣿⣿⣿⣿⣼⡏⠀⠈⠑⢤⣹⡿⣿⣯⠻⢿⣿⣿⣿⣽⠿⢟⣃⣀⣀⡨⣏⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⣾⣾⠁⠀⠈⢹⣿⣿⠟⠀⠀⠀⠀⠀⠈⠛⢾⣿⡆⣶⣿⣿⠗⠒⢉⣉⣉⣙⣛⢿⣧⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⢹⣿⠀⠀⢷⡀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⣿⣿⣷⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠈⠿⣄⠀⣸⣿⣄⣻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏⣉⣉⣉⣉⣉⣿⣏⣉⣉⣉⣉⣉⣉⣙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠙⢷⣌⠧⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⣟⣏⣿⣷⡇⢸⣿⣿⣿⣿⣿⠆⣿⠀⠿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                                 
          
██╗      ██████╗  ██████╗ ██╗███╗   ██╗    ██████╗  █████╗  ██████╗ ███████╗                     
██║     ██╔═══██╗██╔════╝ ██║████╗  ██║    ██╔══██╗██╔══██╗██╔════╝ ██╔════╝                     
██║     ██║   ██║██║  ███╗██║██╔██╗ ██║    ██████╔╝███████║██║  ███╗█████╗                       
██║     ██║   ██║██║   ██║██║██║╚██╗██║    ██╔═══╝ ██╔══██║██║   ██║██╔══╝                       
███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║    ██║     ██║  ██║╚██████╔╝███████╗                     
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝                     
                                                                                   
=================================================================================================
''') 
    print("Silahkan masukkan \033[4musername\033[m dan \033[4mpassword\033[m")

    # Mengecek apakah username dan password sesuai dengan kondisi
    cek_username = input("Masukkan username: ")
    cek_password = input("Masukkan password: ")
    
    return cek_username == "admin" and cek_password == "admin"


percobaan_login = 0

while percobaan_login < 3:
    if cek_admin():
        print("\nLogin berhasil!\n")
        break
    else:
        print("\n\033[4mUsername atau password salah. Coba lagi.\033[m")
        percobaan_login += 1

if percobaan_login == 3:
    print("\nAnda telah melebihi batas percobaan login. Program berhenti.\n")
else:
    while True:

        tampilkan_menu()
        pilihan = input("Pilih menu (1-8): ")

        if pilihan == '1':
            tampilkan_anggota(db_anggota, "Anggota")
        elif pilihan == '2':
            tambah_anggota(db_anggota)
        elif pilihan == '3':
            ubah_anggota(db_anggota)
        elif pilihan == '4':
            hapus_anggota(db_anggota)
        elif pilihan == '5':
            urutkan_anggota(db_anggota)
        elif pilihan == '6':
            kalkulasi_imt(db_anggota)
        elif pilihan == '7':
            tampilkan_anggota(db_pelatih, "Pelatih")
        elif pilihan == '8':
            print("\nProgram keluar. Sampai jumpa!\n")
            break
        else:
            print("Menu tidak valid. Silakan pilih lagi.")

