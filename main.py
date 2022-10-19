from hashlib import sha256
import os
import datetime
import pwinput
os.system('cls')

id_file = open("id.txt", "r+")
pin_file = open("pin.txt", "r+")
balances_file = open("bin.txt", "r+")
name_file = open("name.txt", "r+")
id_other_file = open("id_other.txt", "r+")
name_other_file = open("name_other.txt", "r+")

id_list = []
for i in id_file.readlines():
    id_list.append(i.strip())

pin_list = []
for i in pin_file.readlines():
    pin_list.append(i.strip())

balances_list = []
for i in balances_file.readlines():
    balances_list.append(int(i.strip()))

kamus = {
    "Penarikan berhasil dilakukan."         : "Withdraw Sucessful.",
    "Saldo Anda sekarang adalah"            : "Your balance is",
    "Maaf, saldo Anda tidak mencukupi."     : "Sorry, your balance is not enough.",
    "Masukkan PIN lama Anda: "              : "Enter your old PIN: ",
    "Masukkan PIN baru Anda: "              : "Enter your new PIN: ",
    "Masukkan PIN baru Anda sekali lagi: "  : "Confirm your new PIN: ",
    "Kedua PIN baru Anda tidak sesuai."     : "Your new PIN does not match.",
    "PIN lama Anda tidak sesuai."           : "Your old PIN does not match.",
    "Masukkan ID: "                         : "Enter your ID: ",
    "ID Anda tidak dikenali."               : "Your ID is not recognized.",
    "Masukkan PIN: "                        : "Enter your PIN: ",
    "PIN yang Anda masukkan salah."         : "Wrong PIN.",
    "Anda sudah memasukkan PIN yang salah sebanyak tiga kali. Akun Anda terblokir."
                                            : "You entered wrong PIN(s) three times. Your account is now blocked.",
    "Menu penarikan cepat (1-5): "          : "Quick withdrawal menu (1-5): ",
    "Menu lain (1-5): "                     : "Other menu (1-5): ",
    "Masukkan nominal uang (rupiah): "      : "Enter the nominal (rupiah): ",
    "1. Penarikan tunai"                    : "1. Withdrawal",
    "2. Transfer"                           : "2. Transfer",
    "3. Ganti PIN"                          : "3. Change PIN",
    "4. Informasi saldo"                    : "4. Balance information",
    "5. Menu lain"                          : "5. Other menus",
    "6. Batal"                              : "6. Cancel",
    "Apakah Anda ingin mencetak resi? (y/n): ": "Do you want a receipt? (y/n): "
}

def tr(a):                      #Untuk menterjemahkan suatu string
    if bahasa == "Indonesia":
        return a
    else:
        if a in kamus:
            return kamus[a]
        else:
            return "TRANSLATION ERROR"

def halaman1():
    print("1. Rp250.000,00", "2. Rp500.000,00", "3. Rp1.000.000,00", "4. Rp1.250.000,00", tr("5. Menu lain"), tr("6. Batal"), sep="\n")

def halaman2():
    print(tr("1. Penarikan tunai"), tr("2. Transfer"), tr("3. Ganti PIN"), tr("4. Informasi saldo"), tr("5. Menu lain"), tr("6. Batal"), sep="\n")

def ubah_format(awal):
    j = 0
    akhir_list = []
    akhir = ""
    for i in awal:
        akhir_list.append(i)
    for i in range(len(awal), 0, -1):
        if j == 0:
            j += 1
            continue
        elif j%3 == 0:
            akhir_list.insert(i, ",")
        j += 1
    akhir_list.append(".00")
    for i in akhir_list:
        akhir += i
    return akhir

def penarikan_tunai(nominal):
    if nominal <= balances_list[indeks]:
        balances_list[indeks] -= nominal
        waktu = datetime.datetime.now()
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
        ganti_pin_tanda_tanya = input(tr("Apakah Anda ingin mengganti password? (y/n): "))
        if ganti_pin_tanda_tanya == True:
            ganti_pin()
        else:
            exit()
    else:
        print(tr("Maaf, saldo Anda tidak mencukupi."))

def transfer():
    jenis_bank = input(tr("Pilih tujuan transfer yang Anda inginkan (BNI/Bank lain): "))
    while jenis_bank

def pin_valid(pin):
    if pin.isnumeric():
        if int(pin) >= 0 and int(pin) < 1000000:
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
        
def informasi_saldo():
    print("SALDO REKENING:" + f" Rp {ubah_format(str(balances_list[indeks]))}")

# Pemilihan Bahasa
bahasa = input("Pilih bahasa yang akan digunakan/Choose a language (Indonesia/English): ")
while bahasa != "Indonesia" and bahasa != "English":
    print("Bahasa salah./Wrong language.")
    bahasa = input("Pilih bahasa yang akan digunakan/Choose a language (Indonesia/English): ")

# Validasi ID
os.system('cls')
id = input(tr("Masukkan ID: "))
while not(id in id_list):
    os.system('cls')
    print(tr("ID Anda tidak dikenali."))
    id = input(tr("Masukkan ID: "))
indeks = id_list.index(id)

# Validasi PIN
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

# Penampilan dan Pemilihan Menu
while True:
    os.system('cls')
    halaman1()
    pilih_menu = input(tr("Menu penarikan cepat (1-5): "))
    if pilih_menu == "1":
        penarikan_tunai(250000)
    elif pilih_menu == "2":
        penarikan_tunai(500000)
    elif pilih_menu == "3":
        penarikan_tunai(1000000)
    elif pilih_menu == "4":
        penarikan_tunai(1250000)
    elif pilih_menu == "5":
        while True:
            os.system('cls')
            halaman2()
            pilih_menu = input(tr("Menu lain (1-5): "))
            if pilih_menu == "1":
                os.system('cls')
                nominal = int(input(tr("Masukkan nominal uang (rupiah): ")))
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
    elif pilih_menu == "6":
        exit()
