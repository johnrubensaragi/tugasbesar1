from hashlib import sha256
import os
import datetime
import pwinput
os.system('cls')
waktu = datetime.datetime.now()

id_file = open("id.txt", "r+")
pin_file = open("pin.txt", "r+")
balances_file = open("bin.txt", "r+")
name_file = open("name.txt", "r+")
id_other_file = open("id_other.txt", "r+")
name_other_file = open("name_other.txt", "r+")
bank_list_file = open("bank.txt", "r")
trial_file = open("trial.txt", "r+")

id_list = []
for i in id_file.readlines():
    id_list.append(i.strip())

pin_list = []
for i in pin_file.readlines():
    pin_list.append(i.strip())

balances_list = []
for i in balances_file.readlines():
    balances_list.append(int(i.strip()))

name_list = []
for i in name_file.readlines():
    name_list.append(i.strip())

id_other_list = []
for i in id_other_file.readlines():
    id_other_list.append(i.strip())

name_other_list = []
for i in name_other_file.readlines():
    name_other_list.append(i.strip())

trial_list = []
for i in trial_file.readlines():
    trial_list.append(i.strip())

nama_bank = {"009" : "BNI",  "002" : "BRI", "008" : "MANDIRI", "011" : "DANAMON", "013" : "PERMATA", "014" : "BCA",
 		    "016" : "MAYBANK", "019" : "BANK PANIN", "022" : "CIMB NIAGA", "028" : "OCB NISP", "031" : "CITIBANK",
            "036" : "CCBINDONESIA", "037" : "ARTHA GRAHA", "046" : "BANK DBS", "050" : "STANCHART", "054" : "BANK CAPITAL",
            "061" : "ANZ", "200" : "BTN"}

kamus = {
    "Penarikan berhasil dilakukan."         : "Withdraw Sucessful.",
    "Saldo Anda sekarang adalah"            : "Your balance is",
    "Maaf, saldo Anda tidak mencukupi."     : "Sorry, your balance is not enough.",
    "Masukkan PIN lama Anda: "              : "Enter your old PIN: ",
    "Masukkan PIN baru Anda: "              : "Enter your new PIN: ",
    "Masukkan PIN baru Anda sekali lagi: "  : "Confirm your new PIN: ",
    "Kedua PIN baru Anda tidak sesuai."     : "Your new PIN does not match.",
    "PIN lama Anda tidak sesuai."           : "Your old PIN does not match.",
    "Masukkan nomor rekening: "             : "Enter your account ID: ",
    "ID Anda tidak dikenali."               : "Your ID is not recognized.",
    "Masukkan PIN: "                        : "Enter your PIN: ",
    "PIN yang Anda masukkan salah."         : "Wrong PIN.",
    "Anda sudah memasukkan PIN yang salah sebanyak tiga kali. Akun Anda terblokir."
                                            : "You entered wrong PIN(s) three times. Your account is now blocked.",
    "Menu penarikan cepat"          : "Quick withdrawal menu: ",
    "5. Menu penarikan cepat"          : "5. Quick withdrawal menu: ",
    "Menu lain"                     : "Other menu: ",
    "Pilih menu (1-5): "                    : "Option (1-5): ",
    "Masukkan nominal uang (rupiah): "      : "Enter the nominal (rupiah): ",
    "1. Penarikan tunai"                    : "1. Withdrawal",
    "2. Transfer"                           : "2. Transfer",
    "3. Ganti PIN"                          : "3. Change PIN",
    "4. Informasi saldo"                    : "4. Balance information",
    "5. Menu lain"                          : "5. Other menus",
    "6. Batal"                              : "6. Cancel",
    "Apakah Anda ingin mencetak resi? (y/n): ": "Do you want a receipt? (y/n): ", 
    "Pilihan tidak tersedia."               : "Option is not available.",
    "Transfer berhasil."                    : "Transfer successful.",
    "Transaksi tidak dapat diproses."       : "Transantion cannot be processed.",
    "Apakah Anda ingin mengganti PIN? (y/n): ": "Do you want to change your PIN? (y/n)"}

def tr(a):                      #Untuk menterjemahkan suatu string
    if bahasa == "1":
        return a
    else:
        if a in kamus:
            return kamus[a]
        else:
            return "TRANSLATION ERROR"

def id_validation():
    os.system('cls')
    id = input(tr("Masukkan nomor rekening: "))
    while not(id in id_list):
        os.system('cls')
        print(tr("ID Anda tidak dikenali."))
        id = input(tr("Masukkan nomor rekening: "))
    indeks = id_list.index(id)

def pin_validation():
    os.system('cls')
    pin = pwinput.pwinput(prompt = tr("Masukkan PIN: "))
    pin_sha256 = sha256(pin.encode('utf-8')).hexdigest()
    percobaan = 1
    while percobaan < 3 and pin_sha256 != pin_list[indeks]:
        os.system('cls')
        print(tr("PIN yang Anda masukkan salah."))
        pin = pwinput.pwinput(prompt = tr("Masukkan PIN: "))
        pin_sha256 = sha256(pin.encode('utf-8')).hexdigest()
        percobaan += 1
    if percobaan == 3:
        print(tr("Anda sudah memasukkan PIN yang salah sebanyak tiga kali. Akun Anda terblokir."))
        exit()

def halaman1():
    print(tr("Menu penarikan cepat"),"1. Rp250.000,00", "2. Rp500.000,00", "3. Rp1.000.000,00", "4. Rp1.250.000,00", tr("5. Menu lain"), tr("6. Batal"), sep="\n")

def halaman2():
    print(tr("Menu lain"), tr("1. Penarikan tunai"), tr("2. Transfer"), tr("3. Ganti PIN"), tr("4. Informasi saldo"), tr("5. Menu penarikan cepat"), tr("6. Batal"), sep="\n")

def main():
    while True:
        os.system('cls')
        halaman1()
        pilih_menu = input(tr("Pilih menu (1-5): "))
        if pilih_menu == "1":
            penarikan_tunai(25000000)
        elif pilih_menu == "2":
            penarikan_tunai(50000000)
        elif pilih_menu == "3":
            penarikan_tunai(100000000)
        elif pilih_menu == "4":
            penarikan_tunai(125000000)
        elif pilih_menu == "5":
            while True:
                os.system('cls')
                halaman2()
                pilih_menu = input(tr("Pilih menu (1-5): "))
                if pilih_menu == "1":
                    os.system('cls')
                    try:
                        nominal = int(input(tr("Masukkan nominal uang (rupiah): ")))*100
                    except:
                        print(tr("Nominal tidak sesuai"))
                        input()
                        main()
                    penarikan_tunai(nominal)
                elif pilih_menu == "2":
                    transfer()
                elif pilih_menu == "3":
                    ganti_pin()
                elif pilih_menu == "4":
                    informasi_saldo()
                elif pilih_menu == "5":
                    break
                elif pilih_menu == "6":
                    exit()
                else:
                    print(tr("Pilihan tidak tersedia."))
        elif pilih_menu == "6":
            exit()
        else:
            print(tr("Pilihan tidak tersedia."))
    
def restart():
    pin_validation()
    main()

def ubah_format(awal):
    if len(awal) == 1:
        return "0,0"+awal
    elif len(awal) == 2:
        return "0,"+awal
    j = 0
    akhir_list = []
    akhir = ""
    for i in awal:
        akhir_list.append(i)
    for i in range(len(awal)-2, 0, -1):
        if j == 0:
            j += 1
            continue
        elif j%3 == 0:
            akhir_list.insert(i, ".")
        j += 1
    akhir_list.insert(len(akhir_list)-2, ",")
    for i in akhir_list:
        akhir += i
    return akhir

def penarikan_tunai(nominal):
    if (nominal % 5000000) == 0 and nominal > 0:
        if nominal <= balances_list[indeks]:
            balances_list[indeks] -= nominal
            print(tr("Penarikan berhasil dilakukan."))
            print(tr("Saldo Anda sekarang adalah"), f"Rp {ubah_format(str(balances_list[indeks]))}")
            balances_file.seek(0)
            for i in balances_list:
                balances_file.writelines(str(i) + "\n")
            balances_file.truncate()
            cetak_resi = input(tr("Apakah Anda ingin mencetak resi? (y/n): "))
            if cetak_resi == "y":
                os.system('cls')
                #Receipt keluar dengan format : tanggal, waktu, dan lokasi ATM, jumlah penarikan, dan sisa saldo
                print("-"*16, "Bank BNI", "-"*16)
                print("TANGGAL " + " "*28 + " WAKTU")
                print(waktu.strftime("%d/%m/%y"+ " "*29 +"%H:%M"))
                print("PENARIKAN:" + " "*6 + f"Rp {ubah_format(str(nominal))}" )
                print("SALDO REKENING:" + f" Rp {ubah_format(str(balances_list[indeks]))}")
                print("-"*42)
                input()
                os.system('cls')
            ganti_pin_tanda_tanya = input(tr("Apakah Anda ingin mengganti PIN? (y/n): "))
            if ganti_pin_tanda_tanya == "y":
                ganti_pin()
                main()
            else:
                restart()
        else:
            print(tr("Maaf, saldo Anda tidak mencukupi."))
            input()
            main()
    else:
        print(tr("Transaksi tidak dapat diproses."))
        input()
        main()

def konfirmasi_transfer(id,name,nominal):
    os.system('cls')
    print("Nomor rekening:", id)
    print("Nama penerima:", name)
    print("Nominal: Rp", ubah_format(str(nominal)))
    print(tr("Tekan 1 jika sudah sesuai."))
    print(tr("Tekan 2 jika tidak sesuai."))
    return input()

def ubah_rekening_tujuan(jenis_bank, id_tujuan, indeks_tujuan):
    if jenis_bank == "1":
            id_tujuan = input("Masukkan nomor rekening tujuan: ")
            if id_tujuan in id_list:
                indeks_tujuan = id_list.index(id_tujuan)
            else:
                print(tr("Nomor rekening tidak ada."))
                input()
                main()
    else:
        print(tr("Masukkan kode bank + nomor rekening tujuan."))
        print(tr("Masukkan 0 untuk melihat daftar kode bank."))
        id_tujuan = input()
        while id_tujuan == 0:
            os.system('cls')
            print(bank_list_file.read())
            input()
            os.system('cls')
            print(tr("Masukkan kode bank + nomor rekening tujuan."))
            print(tr("Masukkan 0 untuk melihat daftar kode bank."))
            id_tujuan = input()
        if id_tujuan in id_other_list:
            indeks_tujuan = id_other_list.index(id_tujuan)
        else:
            print(tr("Nomor rekening tidak ada."))
            input()
            main()

def ubah(jenis_bank, id_tujuan, indeks_tujuan, nominal):
    os.system('cls')
    print(tr("1. Ubah nomor rekening"))
    print(tr("2. Ubah nominal"))
    pilihan = input()
    while pilihan != "1" and pilihan != "2":
        os.system('cls')
        print(tr("Pilihan tidak tersedia."))
        print(tr("1. Ubah nomor rekening"))
        print(tr("2. Ubah nominal"))
        pilihan = input()
    if pilihan == "1":
        ubah_rekening_tujuan(jenis_bank, id_tujuan, indeks_tujuan)
    else:
        nominal = int(input("Masukkan nominal transfer: "))*100
        
def transfer():
    # CEK DULU NOMINALNYA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
    os.system('cls')
    print("1. BNI", tr("2. Bank lain"), sep="\n")
    jenis_bank = input(tr("Pilih tujuan transfer yang Anda inginkan: "))
    while jenis_bank != "1" and jenis_bank != "2":
        os.system('cls')
        print(tr("Pilihan tidak tersedia."))
        print("1. BNI", "2. Bank lain", sep="\n")
        jenis_bank = input(tr("Pilih tujuan transfer yang Anda inginkan: "))
    if jenis_bank == "1":
        id_tujuan = input("Masukkan nomor rekening tujuan: ")
        if id_tujuan == id:
            print(tr("Anda tidak bisa transfer ke rekening sendiri."))
            input()
            main()
        elif id_tujuan in id_list:
            indeks_tujuan = id_list.index(id_tujuan)
        else:
            print(tr("Nomor rekening tidak ada."))
            input()
            main()
    else:
        print(tr("Masukkan kode bank + nomor rekening tujuan."))
        print(tr("Masukkan 0 untuk melihat daftar kode bank."))
        id_tujuan = input()
        while id_tujuan == "0":
            os.system('cls')
            print(bank_list_file.read())
            input()
            os.system('cls')
            print(tr("Masukkan kode bank + nomor rekening tujuan."))
            print(tr("Masukkan 0 untuk melihat daftar kode bank."))
            id_tujuan = input()
        if id_tujuan in id_other_list:
            indeks_tujuan = id_other_list.index(id_tujuan)
        else:
            print(tr("Nomor rekening tidak ada."))
            input()
            main()
    nominal = int(input(tr("Masukkan nominal transfer: ")))*100
    # KONFIRMASI
    if jenis_bank == "1":
        while konfirmasi_transfer(id_tujuan, name_list[indeks_tujuan], nominal) != "1":
            ubah(jenis_bank, id_tujuan, indeks_tujuan, nominal)
    else:
        while konfirmasi_transfer(id_tujuan[3:], name_other_list[indeks_tujuan], nominal) != "1":
            ubah(jenis_bank, id_tujuan, indeks_tujuan, nominal)
    if nominal >= 5000000:
        if nominal <= balances_list[indeks]:
            balances_list[indeks] -= nominal
            if jenis_bank == "1":
                balances_list[indeks_tujuan] += nominal
                balances_file.seek(0)
                for i in balances_list:
                    balances_file.writelines(str(i) + "\n")
                balances_file.truncate()
            print(tr("Transfer berhasil."))
            while True:
                cetak_resi = input(tr("Apakah Anda ingin mencetak resi? (y/n): "))
                if cetak_resi == "y":
                    os.system('cls')
                    print("-"*16, "Bank BNI", "-"*16)
                    print("TANGGAL " + " "*28 + " WAKTU")
                    print(waktu.strftime("%d/%m/%y"+ " "*29 +"%H:%M"))
                    print("-"*13, "TRANSFER DARI", "-"*14)
                    print("BANK: BNI", f"NAMA: {name_list[indeks]}", f"NO. REK: {id}", sep="\n")
                    print("-"*19, "KE", "-"*19)
                    if jenis_bank == "1":
                        print("BANK: BNI" , f"NAMA: {name_list[indeks_tujuan]}", f"NO. REK: {id_tujuan}" , f"JUMLAH: Rp {ubah_format(str(nominal))}", sep="\n")
                    else:
                        print(f"BANK: {nama_bank[id_tujuan[:3]]}"  , f"NAMA: {name_other_list[indeks_tujuan]}", f"NO. REK: {id_tujuan[3:]}" , f"JUMLAH: Rp {ubah_format(str(nominal))}", sep="\n")
                    print("-"*42)
                    input()
                    break
                elif cetak_resi == "n":
                    break
                print(tr("Input tidak sesuai."))
        else:
            print(tr("Maaf, saldo Anda tidak mencukupi."))
            input()
            main()
    else:
        print(tr("Transaksi tidak dapat diproses."))
        input()
        main()

def pin_valid(pin):
    if pin.isnumeric():
        if len(pin) == 6:
            return True
    return False

def ganti_pin():
    os.system('cls')
    pin_lama = pwinput.pwinput(prompt = tr("Masukkan PIN lama Anda: "))
    while not pin_valid(pin_lama):
        os.system('cls')
        print(tr("PIN harus terdiri dari 6 digit."))
        pin_lama = pwinput.pwinput(prompt = tr("Masukkan PIN lama Anda: "))
    pin_sha256 = sha256(pin_lama.encode('utf-8')).hexdigest()

    if pin_sha256 == pin_list[indeks]:
        os.system('cls')
        pin_baru1 = pwinput.pwinput(prompt = tr("Masukkan PIN baru Anda: "))
        while not pin_valid(pin_baru1):
            os.system('cls')
            print(tr("PIN harus terdiri dari 6 digit."))
            pin_baru1 = pwinput.pwinput(prompt = tr("Masukkan PIN baru Anda: "))

        os.system('cls')
        pin_baru2 = pwinput.pwinput(prompt = tr("Masukkan PIN baru Anda sekali lagi: "))
        while not pin_valid(pin_baru2):
            os.system('cls')
            print(tr("PIN harus terdiri dari 6 digit."))
            pin_baru2 = pwinput.pwinput(prompt = tr("Masukkan PIN baru Anda sekali lagi: "))
        
        if pin_baru1 == pin_baru2:
            pin_sha256 = sha256(pin_baru1.encode('utf-8')).hexdigest()
            pin_list[indeks] = pin_sha256
            pin_file.seek(0)
            for i in pin_list:
                pin_file.writelines(i + "\n")
            pin_file.truncate()
        else:
            print(tr("Kedua PIN baru Anda tidak sesuai."))
    else:
        print(tr("PIN lama Anda tidak sesuai."))
    exit()
        
def informasi_saldo():
    print("SALDO REKENING:" + f" Rp {ubah_format(str(balances_list[indeks]))}")
    input()

"""
bahasa = ""
while bahasa != "1" and bahasa != "2":
    print("1. Indonesia", "2. English", sep="\n")
    bahasa = input("Pilih bahasa / Choose a language: ")
    if bahasa != "1" and bahasa != "2":
        os.system('cls')
        print("Pilihan tidak tersedia./Option is not available.")
"""

# Validasi ID
os.system('cls')
id = input("Masukkan nomor rekening Anda / Enter your account number: ")
while not(id in id_list) or not(id.isdecimal()):
    os.system('cls')
    if "*"+id in id_list:
        print("Nomor rekening Anda terblokir. / Your account is blocked.")
    else:
        print("Nomor rekening Anda tidak dikenali. / Your account is not recognized.")
    id = input("Masukkan nomor rekening Anda / Enter your account number: ")
indeks = id_list.index(id)

# Pemilihan Bahasa
os.system('cls')
print("1. Indonesia", "2. English", sep="\n")
bahasa = input("Pilih bahasa / Choose a language: ")
while bahasa != "1" and bahasa != "2":
    os.system('cls')
    print("Pilihan tidak tersedia./Option is not available.")
    print("1. Indonesia", "2. English", sep="\n")
    bahasa = input("Pilih bahasa / Choose a language: ")

# Validasi PIN
os.system('cls')
pin = pwinput.pwinput(prompt = tr("Masukkan PIN: "))
while not pin_valid(pin):
    os.system('cls')
    print(tr("PIN harus terdiri dari 6 digit."))
    pin = pwinput.pwinput(prompt = tr("Masukkan PIN: "))
pin_sha256 = sha256(pin.encode('utf-8')).hexdigest()

percobaan = int(trial_list[indeks])+1
trial_list[indeks] = str(percobaan)
trial_file.seek(0)
for i in trial_list:
    trial_file.writelines(i + "\n")
trial_file.truncate()

while percobaan < 3 and pin_sha256 != pin_list[indeks]:
    os.system('cls')
    print(tr("PIN yang Anda masukkan salah."))
    print(tr("Jika Anda salah memasukkan PIN sebanyak 3 (tiga) kali, akun Anda akan terblokir"))
    pin = pwinput.pwinput(prompt = tr("Masukkan PIN: "))
    while not pin_valid(pin):
        os.system('cls')
        print(tr("PIN harus terdiri dari 6 digit."))
        pin = pwinput.pwinput(prompt = tr("Masukkan PIN: "))
    pin_sha256 = sha256(pin.encode('utf-8')).hexdigest()
    percobaan = int(trial_list[indeks])+1
    trial_list[indeks] = str(percobaan)
    trial_file.seek(0)
    for i in trial_list:
        trial_file.writelines(i + "\n")
    trial_file.truncate()
if percobaan == 3 and pin_sha256 != pin_list[indeks]:
    id_list[indeks] = "*" + id_list[indeks]
    id_file.seek(0)
    for i in id_list:
        id_file.writelines(i + "\n")
    id_file.truncate()
    print(tr("Anda sudah memasukkan PIN yang salah sebanyak 3 (tiga) kali. Akun Anda terblokir."))
    exit()
trial_list[indeks] = "0"
trial_file.seek(0)
for i in trial_list:
    trial_file.writelines(i + "\n")
trial_file.truncate()
# Penampilan dan Pemilihan Menu
main()