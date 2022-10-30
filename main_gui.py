from tkinter import *
from hashlib import sha256
import os
import datetime
import time
os.system('cls')
waktu = datetime.datetime.now()

# User Interface
window = Tk()
window.title(" " * 128 + "ATM BNI")
window.geometry("900x800+300+20")
window.minsize(900, 800)
window.maxsize(900, 800)
main = Frame(window, width = 900, height = 800, bg = "grey")
main.grid(row = 0, column = 0)

# User Data (membuka file dan menyimpan data dalam array)
id_file = open("id.txt", "r+")
pin_file = open("pin.txt", "r+")
pin_sebelum_file = open("pin_sebelum.txt", "r+")
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

pin_sebelum_list = []
for i in pin_sebelum_file.readlines():
    pin_sebelum_list.append(i.strip())

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

# nama bank
nama_bank = {"009" : "BNI",  "002" : "BRI", "008" : "MANDIRI", "011" : "DANAMON", "013" : "PERMATA", "014" : "BCA",
 		    "016" : "MAYBANK", "019" : "BANK PANIN", "022" : "CIMB NIAGA", "028" : "OCB NISP", "031" : "CITIBANK",
            "036" : "CCBINDONESIA", "037" : "ARTHA GRAHA", "046" : "BANK DBS", "050" : "STANCHART", "054" : "BANK CAPITAL",
            "061" : "ANZ", "200" : "BTN"}

# kamus untuk terjemahan
kamus = {
    "Penarikan berhasil dilakukan."         : "Withdraw Successful.",
    "Saldo Anda sekarang adalah"            : "Your balance is",
    "Maaf, saldo Anda tidak mencukupi."     : "Sorry, your balance is not enough.",
    "Masukkan PIN lama Anda: "              : "Enter your old PIN: ",
    "Masukkan PIN baru Anda: "              : "Enter your new PIN: ",
    "Masukkan PIN baru Anda sekali lagi: "  : "Confirm your new PIN: ",
    "Kedua PIN baru Anda tidak sesuai."     : "Your new PIN does not match.",
    "PIN lama Anda tidak sesuai."           : "Your old PIN does not match.",
    "Pilih bank tujuan transfer:"           : "Choose transfer destination bank:",
    "2. Bank Lain"                          : "2. Other banks",
    "Masukkan nomor rekening tujuan"        : "Enter transfer destination account number",
    "Masukkan nominal transfer:"            : "Enter the transfer amount:",
    "Masukkan nomor rekening: "             : "Enter your account ID: ",
    "ID Anda tidak dikenali."               : "Your ID is not recognized.",
    "Nomor rekening tidak ada."             : "Account number does not exist.",
    "Nomor rekening: "                      : "Account number: ",
    "Nama penerima: "                       : "Recipent's name: ",
    "Tekan 1 jika sudah sesuai."            : "Press 1 if correct.",
    "Tekan 2 jika tidak sesuai."            : "Press 2 if incorect.",
    "Masukkan PIN:"                         : "Enter your PIN: ",
    "PIN yang Anda masukkan salah."         : "Wrong PIN.",
    "Jika Anda salah memasukkan PIN sebanyak 3 (tiga) kali," : "If you enter the wrong pin for three (3) times in a row,",
    "akun Anda akan terblokir"              : "your account will be blocked",
    "Akun Anda terblokir."                  : "Your account has been blocked.",
    "Anda sudah memasukkan PIN yang salah sebanyak tiga kali. Akun Anda terblokir."
                                            : "You entered wrong PIN(s) three times. Your account is now blocked.",
    "Menu penarikan cepat"                  : "Quick withdrawal menu: ",
    "5. Menu penarikan cepat"               : "5. Quick withdrawal menu",
    "Menu lain"                             : "Other menu: ",
    "Pilih menu (1-5): "                    : "Option (1-5): ",
    "Masukkan nominal uang (rupiah) "       : "Enter the nominal (rupiah) ",
    "Maksimal Rp1.250.000,00"               : "Maximum Rp1.250.000,00",
    "1. Penarikan tunai"                    : "1. Withdrawal",
    "2. Transfer"                           : "2. Transfer",
    "3. Ganti PIN"                          : "3. Change PIN",
    "4. Informasi saldo"                    : "4. Balance information",
    "5. Menu lain"                          : "5. Other menus",
    "Apakah Anda ingin mencetak resi?: "    : "Do you want a receipt?: ",
    "1. Ya"                                 : "1. Yes",
    "2. Tidak"                              : "2. No",
    "Pilihan tidak tersedia."               : "Option is not available.",
    "Transaksi sedang diproses."            : "The transaction is being processed.",
    "Harap tunggu..."                       : "Please wait...",
    "Transfer berhasil."                    : "Transfer successful.",
    "Transaksi tidak dapat diproses."       : "Transantion cannot be processed.",
    "Apakah Anda ingin mengganti PIN?: "    : "Do you want to change your PIN? ",
    "PIN berhasil diganti."                 : "Your PIN has been changed.",
    "SALDO REKENING:"                       : "ACCOUNT BALANCE:",
    "Tekan Enter untuk kembali ke menu utama.":"Press Enter to go to the main menu.",
    "Tekan Cancel untuk keluar."            : "Press Cancel to exit."}

def tr(a):
    if bahasa == "1":
        return a
    else:
        if a in kamus:
            return kamus[a]
        else:
            return "TRANSLATION ERROR"

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

def PIN_trial():
    global wrongPIN, pin, state
    wrongPIN = True
    layar.delete('1.0', END)
    layar.insert(END, f"{tr('PIN yang Anda masukkan salah.')}\n")
    layar.insert(END, f"{tr('Jika Anda salah memasukkan PIN sebanyak 3 (tiga) kali,')}\n")
    layar.insert(END, f"{tr('akun Anda akan terblokir')}\n")
    layar.insert(END, tr("Masukkan PIN:")+"\n")
    pin = ""
    state = "PIN"

def penarikan_tunai():
    global state, last_state
    if (nominal % 5000000) == 0 and nominal > 0 and nominal <= 125000000:
        if nominal <= balances_list[indeks]:
            layar.delete('1.0', END)
            layar.insert(END, f"{tr('Transaksi sedang diproses.')}\n")
            layar.insert(END, f"{tr('Harap tunggu...')}\n")
            tksleep(2)
            if pin_sha256 == pin_list[indeks]:
                tksleep(3)
                balances_list[indeks] -= nominal
                layar.delete('1.0', END)
                layar.insert(END, f"{tr('Penarikan berhasil dilakukan.')}\n")
                layar.insert(END, f"{tr('Saldo Anda sekarang adalah')}\n")
                layar.insert(END, f"Rp {ubah_format(str(balances_list[indeks]))}\n\n")
                balances_file.seek(0)
                for i in balances_list:
                    balances_file.writelines(str(i) + "\n")
                balances_file.truncate()
                if not penarikan_cepat:
                    state = "resi_tarik"
                    layar.insert(END, f"{tr('Apakah Anda ingin mencetak resi?: ')}\n")
                    layar.insert(END, f"{tr('1. Ya')}\n")
                    layar.insert(END, f"{tr('2. Tidak')}\n")
                else:
                    state = "ganti pin?"
                    layar.insert(END, f"{tr('Apakah Anda ingin mengganti PIN?: ')}\n")
                    layar.insert(END, f"{tr('1. Ya')}\n")
                    layar.insert(END, f"{tr('2. Tidak')}\n")
            else:
                last_state = "penarikan_tunai"
                PIN_trial()
        else:
            layar.delete("1.0", END)
            layar.insert(END, tr("Maaf, saldo Anda tidak mencukupi.") + "\n" + tr('Tekan Enter untuk kembali ke menu utama.') + "\n" + tr("Tekan Cancel untuk keluar."))
            state = "penarikan_tunai_gagal"
    else:
        layar.delete("1.0", END)
        layar.insert(END, "\n"+ tr("Transaksi tidak dapat diproses.") + "\n" + tr("Tekan Enter untuk kembali ke menu utama.") + "\n" + tr("Tekan Cancel untuk keluar."))
        state = "penarikan_tunai_gagal"

def tujuan_transfer():
    global state, indeks_tujuan, nominal_str, nama, jenis_bank, id_tujuan, ubah
    layar.delete("1.0", END)
    if jenis_bank == "1":
        if id_tujuan == id:
            state = "transfer_gagal"
            layar.insert(END, tr("Anda tidak bisa transfer ke rekening sendiri.") + "\n")
            layar.insert(END, {tr("Tekan Enter untuk kembali ke menu utama.")} + "\n" + tr("Tekan Cancel untuk keluar."))
        elif id_tujuan in id_list:
            indeks_tujuan = id_list.index(id_tujuan)
            nama = name_list[indeks_tujuan]
            if ubah:
                state = "transfer(konfirmasi)"
                konfirmasi_transfer()
            else:
                state = "transfer(nominal)"
                layar.delete("1.0", END)
                layar.insert(END, tr("Masukkan nominal transfer:")+"\n")
                nominal_str = ""
        else:
            state = "transfer_gagal"
            layar.insert(END, tr("Nomor rekening tidak ada.") + "\n")
            layar.insert(END, tr("Tekan Enter untuk kembali ke menu utama.")+ "\n" + tr("Tekan Cancel untuk keluar."))
    else:
        if id_tujuan in id_other_list:
            indeks_tujuan = id_other_list.index(id_tujuan)
            nama = name_other_list[indeks_tujuan]
            state = "transfer(nominal)"
            layar.delete("1.0", END)
            layar.insert(END, tr("Masukkan nominal transfer:")+"\n")
            nominal_str = ""
        else:
            state = "transfer_gagal"
            layar.insert(END, tr("Nomor rekening tidak ada." + "\n"))
            layar.insert(END, tr("Tekan Enter untuk kembali ke menu utama.") + "\n" + tr("Tekan Cancel untuk keluar."))

def konfirmasi_transfer():
    global id_tujuan, nama, nominal, jenis_bank
    layar.delete("1.0", END)
    if jenis_bank == "1":
        layar.insert(END, f"{tr('Nomor rekening: ')} {id_tujuan}\n")
    else:
        layar.insert(END, f"{tr('Nomor rekening: ')} {id_tujuan[3:]}\n")   
    layar.insert(END, f"{tr('Nama penerima: ')} {nama}\n")
    layar.insert(END, f"Nominal: Rp {ubah_format(str(nominal))}\n")
    layar.insert(END, f"{tr('Tekan 1 jika sudah sesuai.')}\n{tr('Tekan 2 jika tidak sesuai.')}")

def validasi_transfer():
    global state, last_state, jenis_bank, nominal, indeks_tujuan, indeks, id
    layar.delete("1.0", END)
    if nominal >= 5000000:
        if nominal <= balances_list[indeks]:
            if pin_sha256 == pin_list[indeks]:
                balances_list[indeks] -= nominal
                if jenis_bank == "1":
                    balances_list[indeks_tujuan] += nominal
                    balances_file.seek(0)
                    for i in balances_list:
                        balances_file.writelines(str(i) + "\n")
                    balances_file.truncate()
                layar.insert(END, tr("Transfer berhasil.")+"\n")
                state = "resi_transfer"
                layar.insert(END, f"{tr('Apakah Anda ingin mencetak resi?: ')}\n")
                layar.insert(END, f"{tr('1. Ya')}\n")
                layar.insert(END, f"{tr('2. Tidak')}\n")
            else:
                last_state = "transfer(validasi)"
                PIN_trial()
        else:
            state = "transfer_gagal"
            layar.delete("1.0", END)
            layar.insert(END, tr("Maaf, saldo Anda tidak mencukupi.") + "\n")
            layar.insert(END, tr("Tekan Enter untuk kembali ke menu utama.") + "\n" + tr("Tekan Cancel untuk keluar."))
            
    else:
        state = "transfer_gagal"
        layar.delete("1.0", END)
        layar.insert(END, tr("Transaksi tidak dapat diproses."))
        layar.insert(END, tr("Tekan Enter untuk kembali ke menu utama.") + "\n" + tr("Tekan Cancel untuk keluar."))

# User Interface part 2
def update_trial_list():
    global percobaan, trial_list, trial_file
    trial_list[indeks] = str(percobaan)
    trial_file.seek(0)
    for i in trial_list:
        trial_file.writelines(i + "\n")
    trial_file.truncate()

def ganti_pin(pin_baru1):
    layar.delete("1.0", END)
    pin_sha256 = sha256(pin_baru1.encode('utf-8')).hexdigest()
    pin_list[indeks] = pin_sha256
    pin_file.seek(0)
    for i in pin_list:
        pin_file.writelines(i + "\n")
    pin_file.truncate()
    pin_sebelum_list[indeks] = pin_baru1
    pin_sebelum_file.seek(0)
    for i in pin_sebelum_list:
        pin_sebelum_file.writelines(i + "\n")
    pin_sebelum_file.truncate()
    layar.insert(END, f"{tr('PIN berhasil diganti.')}\n{tr('Tekan Enter untuk kembali ke menu utama.')}\n{tr('Tekan Cancel untuk keluar.')}")

def input_(num):
    global state, last_state, id, pin, pin_sha256, bahasa, wrongPIN, percobaan, nominal, nominal_str, pin_lama, pin_baru1, pin_baru2, id_tujuan, jenis_bank, penarikan_cepat, ubah
    print(state)

    if state == "ID":
        id += str(num)
        layar.insert(END, str(num))

    elif state == "Bahasa" and (num == 1 or num == 2):
        bahasa = str(num)
        state = "PIN"
        layar.delete('1.0', END) # Ekuivalen dengan os.system('cls')
        wrongPIN = False
        layar.insert(END, tr("Masukkan PIN:")+"\n")
        pin = ""

    elif state == "PIN":
        pin += str(num)
        layar.insert(END, "X")
        if len(pin) == 6:
            tksleep(1)
            pin_sha256 = sha256(pin.encode('utf-8')).hexdigest()
            percobaan = int(trial_list[indeks])+1
            print(percobaan)
            update_trial_list()
            if pin_sha256 == pin_list[indeks]:
                percobaan = 0
                update_trial_list()
                if wrongPIN:
                    if last_state == "penarikan_tunai":
                        penarikan_tunai()
                    if last_state == "transfer(validasi)":
                        validasi_transfer()
                    if last_state == "main2":
                        state = "main2"
                        penarikan_cepat = False
                        layar.delete("1.0", END)
                        layar.insert("1.0", f'{tr("Menu lain")}\n{tr("1. Penarikan tunai")}\n{tr("2. Transfer")}\n{tr("3. Ganti PIN")}\n{tr("4. Informasi saldo")}\n{tr("5. Menu penarikan cepat")}')
                    if last_state == "gantipin(baru2)":
                        ganti_pin(pin_baru1)
            if not wrongPIN:
                layar.delete('1.0', END)
                state = "main1"
                layar.insert(END, f"{tr('Menu penarikan cepat')}\n1. Rp250.000,00\n2. Rp500.000,00\n3. Rp1.000.000,00\n4. Rp1.250.000,00\n{tr('5. Menu lain')}")
            if wrongPIN and pin_sha256 != pin_list[indeks]:
                if percobaan < 3:
                    PIN_trial()
                else:
                    id_list[indeks] = "*" + id_list[indeks]
                    id_file.seek(0)
                    for i in id_list:
                        id_file.writelines(i + "\n")
                    id_file.truncate()
                    layar.delete('1.0', END)
                    layar.insert(END, tr("Anda sudah memasukkan PIN yang salah sebanyak 3 (tiga) kali.")+"\n")
                    layar.insert(END, tr('Akun Anda terblokir.')+"\n")
                    tksleep(5)
                    restart()

    elif state == "main1":
        if num == 1:
            nominal = 25000000
            penarikan_cepat = True
            penarikan_tunai()
        elif num == 2:
            nominal = 50000000
            penarikan_cepat = True
            penarikan_tunai()
        elif num == 3:
            nominal = 100000000
            penarikan_cepat = True
            penarikan_tunai()
        elif num == 4:
            nominal = 125000000
            penarikan_cepat = True
            penarikan_tunai()
        elif num == 5:
            state = "main2"
            penarikan_cepat = False
            layar.delete("1.0", END)
            layar.insert("1.0", f'{tr("Menu lain")}\n{tr("1. Penarikan tunai")}\n{tr("2. Transfer")}\n{tr("3. Ganti PIN")}\n{tr("4. Informasi saldo")}\n{tr("5. Menu penarikan cepat")}')
    elif state == "main2":
        if num == 1:
            state = "penarikan_tunai"
            layar.delete("1.0", END)
            layar.insert(END, tr("Masukkan nominal uang (rupiah) ")+"\n")
            layar.insert(END, tr("Maksimal Rp1.250.000,00")+"\n")
            nominal_str = ""
        elif num == 2:
            state = "transfer(awal)"
            layar.delete("1.0", END)
            layar.insert(END, tr("Pilih bank tujuan transfer:") + "\n")
            layar.insert(END, f"1. BNI\n{tr('2. Bank Lain')}")
        elif num == 3:
            state = "gantipin(lama)"
            layar.delete("1.0", END)
            layar.insert(END, tr("Masukkan PIN lama Anda: ")+"\n")
            pin_lama = ""
        elif num == 4:
            if pin_sha256 == pin_list[indeks]:    
                layar.delete("1.0", END)
                layar.insert(END, (tr("SALDO REKENING:") + f" Rp {ubah_format(str(balances_list[indeks]))}\n"))
                layar.insert(END, f"{tr('Tekan Enter untuk kembali ke menu utama.')}\n{tr('Tekan Cancel untuk keluar.')}")
                state = "informasi_saldo"
            else:
                last_state = "main2"
                PIN_trial()
        elif num == 5:
            state = "main1"
            layar.delete("1.0", END)
            layar.insert(END, f"{tr('Menu penarikan cepat')}\n1. Rp250.000,00\n2. Rp500.000,00\n3. Rp1.000.000,00\n4. Rp1.250.000,00\n{tr('5. Menu lain')}")
    elif state == "resi_tarik":
        if num == 1 or num == 2:
            if num == 1:
                print("Cetak resinya!")
                layar.delete("1.0", END)
                layar.configure(bg = "white", fg = "black")
                layar.insert(END, "-"*16+" Bank BNI "+"-"*16+"\n")
                layar.insert(END, "TANGGAL " + " "*28 + " WAKTU\n")
                layar.insert(END, waktu.strftime("%d/%m/%y"+ " "*29 +"%H:%M")+"\n")
                layar.insert(END, "PENARIKAN:" + " "*6 + f"Rp {ubah_format(str(nominal))}\n" )
                layar.insert(END, "SALDO REKENING:" + f" Rp {ubah_format(str(balances_list[indeks]))}\n")
                layar.insert(END, "-"*42 + "\n")
                tksleep(10)
                layar.delete("1.0", END)
                layar.configure(bg = "blue", fg = "white")
            state = "ganti pin?"
            layar.insert(END, f"{tr('Apakah Anda ingin mengganti PIN?: ')}\n")
            layar.insert(END, f"{tr('1. Ya')}\n")
            layar.insert(END, f"{tr('2. Tidak')}\n")
    
    elif state == "resi_transfer":
        if num == 1 or num == 2:
            if num == 1:
                layar.delete("1.0", END)
                layar.configure(bg = "white", fg = "black")
                layar.insert(END, "-"*16+ " Bank BNI "+ "-"*16+"\n")
                layar.insert(END, "TANGGAL " + " "*28 + " WAKTU"+"\n")
                layar.insert(END, waktu.strftime("%d/%m/%y"+ " "*29 +"%H:%M")+"\n")
                layar.insert(END, "-"*13 +" TRANSFER DARI "+ "-"*14+"\n")
                layar.insert(END, "BANK: BNI\n")
                layar.insert(END, f"NAMA: {name_list[indeks]}\n")
                layar.insert(END, f"NO. REK: {id}\n")
                layar.insert(END, "-"*19 +" KE "+ "-"*19+"\n")
                if jenis_bank == "1":
                    layar.insert(END, "BANK: BNI\n")
                    layar.insert(END, f"NAMA: {name_list[indeks_tujuan]}\n")
                    layar.insert(END, f"NO. REK: {id_tujuan}\n")
                    layar.insert(END, f"JUMLAH: Rp {ubah_format(str(nominal))}\n")
                else:
                    layar.insert(END, f"BANK: {nama_bank[id_tujuan[:3]]}\n")
                    layar.insert(END, f"NAMA: {name_other_list[indeks_tujuan]}\n")
                    layar.insert(END, f"NO. REK: {id_tujuan[3:]}\n")
                    layar.insert(END, f"JUMLAH: Rp {ubah_format(str(nominal))}\n")
                layar.insert(END, "-"*42)
                tksleep(10)
                layar.delete("1.0", END)
                layar.configure(bg = "blue", fg = "white")
            state = "ganti pin?"
            layar.insert(END, f"{tr('Apakah Anda ingin mengganti PIN?: ')}\n")
            layar.insert(END, f"{tr('1. Ya')}\n")
            layar.insert(END, f"{tr('2. Tidak')}\n")

    elif state == "penarikan_tunai":
        nominal_str += str(num)
        layar.insert(END, num)
        print(nominal_str)
    
    elif state == "transfer(awal)":
        ubah = False
        if num == 1:
            layar.delete("1.0", END)
            state = "transfer(id)"
            layar.insert(END, tr("Masukkan nomor rekening tujuan") + "\n")
            jenis_bank = "1"
            id_tujuan = ""
        elif num == 2:
            layar.delete("1.0", END)
            state = "transfer(id_other)"
            layar.insert(END, tr("Masukkan kode bank + nomor rekening tujuan") + "\n")
            layar.insert(END, tr("Tekan Enter tanpa masukan rekening") + "\n")
            layar.insert(END, tr("untuk melihat daftar bank.") + "\n")
            jenis_bank = "2"
            id_tujuan = ""
    elif state == "transfer(id)" or state == "transfer(id_other)":
        layar.insert(END, num)
        id_tujuan += str(num)
    elif state == "transfer(nominal)":
        layar.insert(END, num)
        nominal_str += str(num)
    elif state == "transfer(konfirmasi)":
        if num == 1:
            state = "transfer(validasi)"
            validasi_transfer()
        else:
            state = "transfer(ubah)"
            print(tr("1. Ubah nomor rekening"))
            print(tr("2. Ubah nominal"))
            layar.delete("1.0", END)
            layar.insert(END, f"{tr('1. Ubah nomor rekening')}\n{tr('2. Ubah nominal')}")
    elif state == "transfer(ubah)":
        if num == 1:
            ubah = True
            layar.delete("1.0", END)
            if jenis_bank == "1":
                state = "transfer(id)"
                layar.insert(END, tr("Masukkan nomor rekening tujuan")+"\n")
                id_tujuan = ""
            else:
                state = "transfer(id_other)"
                layar.insert(END, tr("Masukkan kode bank + nomor rekening tujuan") + "\n")
                layar.insert(END, tr("Tekan Enter tanpa masukan rekening") + "\n")
                layar.insert(END, tr("untuk melihat daftar bank.") + "\n")
                id_tujuan = ""
        elif num == 2:
            ubah = True
            layar.delete("1.0", END)
            state = "transfer(nominal)"
            layar.delete("1.0", END)
            layar.insert(END, tr("Masukkan nominal transfer:")+"\n")
            nominal_str = ""

    elif state == "ganti pin?":
        if num == 1:
            state = "gantipin(lama)"
            layar.delete("1.0", END)
            layar.insert(END, tr("Masukkan PIN lama Anda: ")+"\n")
            pin_lama = ""
        else:
            state = "PIN"
            layar.delete('1.0', END) # Ekuivalen dengan os.system('cls')
            wrongPIN = False
            layar.insert(END, tr("Masukkan PIN:")+"\n")
            pin = ""
    elif state == "gantipin(lama)":
        pin_lama += str(num)
        layar.insert(END, "X")
        if len(pin_lama) == 6:
            tksleep(1)
            layar.delete("1.0", END)
            layar.insert(END,tr("Masukkan PIN baru Anda: ")+"\n")
            pin_baru1 = ""
            state = "gantipin(baru1)"
            #else:
            #    layar.delete("1.0", END)
            #    layar.insert(END, tr("PIN lama Anda tidak sesuai.")+"\n")
            #    layar.insert(END, tr("Masukkan PIN lama Anda: ")+"\n")
            #    pin_lama = ""
    elif state == "gantipin(baru1)":
        pin_baru1 += str(num)
        layar.insert(END, "X")
        if len(pin_baru1) == 6:
            tksleep(1)
            pin_sha256 = sha256(pin_baru1.encode('utf-8')).hexdigest()
            if pin_sha256 == pin_list[indeks]:
                layar.delete("1.0", END)
                layar.insert(END, tr("Masukkan PIN yang")+"\n")
                layar.insert(END, tr("belum digunakan sebelumnya:")+"\n")
                pin_baru1 = ""
            else:
                layar.delete("1.0", END)
                layar.insert(END, tr("Masukkan PIN baru Anda sekali lagi: ")+"\n")
                pin_baru2 = ""
                state = "gantipin(baru2)"
    elif state == "gantipin(baru2)":
        pin_baru2 += str(num)
        layar.insert(END, "X")
        if len(pin_baru2) == 6:
            tksleep(1)
            if pin_baru1 == pin_baru2:
                print(pin_lama)
                pin_sha256 = sha256(pin_lama.encode('utf-8')).hexdigest()
                print(pin_sha256)
                if pin_sha256 == pin_list[indeks]:
                    ganti_pin(pin_baru1)
                else:
                    last_state = "gantipin(baru2)"
                    PIN_trial()
            else:
                layar.insert(END, tr("Kedua PIN baru Anda tidak sesuai."))

def tksleep(secs):
    global state
    last_state = state
    print("last state =", last_state)
    state = ""
    print("current state =", state)
    window.update()
    time.sleep(secs)
    state = last_state

def restart():
    global state, id
    print("cancel")
    layar.delete(1.0, END)
    layar.insert(END, "Transaksi selesai.\n")
    layar.insert(END, "Transaction done.\n")
    tksleep(5)
    layar.delete("1.0", END)
    state = "ID"
    id = ""
    print("current state =", state)
    layar.insert(END,"Masukkan nomor rekening Anda\nEnter your account number\n\n")

def input_clear():
    global state, pin, id, pin_lama, pin_baru1, pin_baru2, id_tujuan
    if state == "PIN":
        layar.delete(f"end-{len(pin)+1}c", END)
        pin = ""
    if state == "ID":
        layar.delete(f"end-{len(id)+1}c", END)
        id = ""
        layar.insert(END, "\n")
    if state == "gantipin(lama)":
        layar.delete(f"end-{len(pin_lama)+1}c", END)
        pin_lama = ""
    if state == "gantipin(baru1)":
        layar.delete(f"end-{len(pin_baru1)+1}c", END)
        pin_baru1 = ""
    if state == "gantipin(baru2)":
        layar.delete(f"end-{len(pin_baru2)+1}c", END)
        pin_baru2 = ""
    if state == "penarikan_tunai":
        layar.delete(f"end-{len(nominal_str)+1}c", END)
        nominal_str = ""
    if state == "transfer(id)" or state == "transfer(id_other)": # ini udah bener or. Jangan diganti.
        layar.delete(f"end-{len(id_tujuan)+1}c", END)
        id_tujuan = ""
    if state == "transfer(nominal)":
        layar.delete(f"end-{len(nominal_str)+1}c", END)
        nominal_str = ""
    layar.insert(END, "\n")

def input_enter():
    global state, id, indeks, nominal, id_tujuan
    if state == "ID":
        if id in id_list:
            indeks = id_list.index(id)
            state = "Bahasa"
            layar.delete('1.0', END)
            layar.insert(END,"Pilih bahasa / Choose a language:\n1. Indonesia\n2. English")
        elif '*'+id in id_list:
            layar.delete('1.0', END)
            layar.insert(END, "Nomor rekening Anda terblokir.\nYour account is blocked.\n\n")
            id = ""
            layar.insert(END, "Masukkan nomor rekening Anda\nEnter your account number\n\n")
        else:
            layar.delete('1.0', END)
            layar.insert(END, "Nomor rekening Anda tidak dikenali.\nYour account is not recognized.\n\n")
            id = ""
            layar.insert(END, "Masukkan nomor rekening Anda\nEnter your account number\n\n")
    elif state == "gantipin(baru2)" or state == "penarikan_tunai_gagal" or state == "informasi_saldo" or state == "transfer_gagal":
        state = "main1"
        layar.delete("1.0", END)
        layar.insert(END, f"{tr('Menu penarikan cepat')}\n1. Rp250.000,00\n2. Rp500.000,00\n3. Rp1.000.000,00\n4. Rp1.250.000,00\n{tr('5. Menu lain')}")
    elif state == "penarikan_tunai":
        nominal = int(nominal_str) * 100
        penarikan_tunai()
    elif state == "transfer(id)":
        tujuan_transfer()
    elif state == "transfer(id_other)":
        if id_tujuan == "":
            layar.delete("1.0", END)
            layar.insert(END, bank_list_file.read())
            layar.insert(END, "Tekan Enter untuk kembali.")
            state = "daftar_bank"
        else:
            tujuan_transfer()
    elif state == "transfer(nominal)":
        print(nominal_str)
        nominal = int(nominal_str) * 100
        state = "transfer(konfirmasi)"
        konfirmasi_transfer()
    elif state == "daftar_bank":
        state = "transfer(id_other)"
        layar.delete("1.0", END)
        layar.insert(END, tr("Masukkan kode bank + nomor rekening tujuan") + "\n")
        layar.insert(END, tr("Tekan Enter tanpa masukan rekening") + "\n")
        layar.insert(END, tr("untuk melihat daftar bank.") + "\n")
        id_tujuan = ""
        


blok_atas = Frame(main, width = 900, height = 800/2, border = 1, relief = RIDGE)
blok_atas.grid(row = 0, column = 0)

blok_bawah = Frame(main, width = 900, height = 800/2, border = 1, relief = RIDGE)
blok_bawah.grid(row = 1, column = 0)
blok_bawah.grid_propagate(False)

blok_bawah_tengah = Frame(blok_bawah, width=500, height = 400, border=1, relief=RIDGE)
blok_bawah_tengah.place(relx = 0.5, rely = 0.5, anchor="center")
blok_bawah_tengah.grid_propagate(False)

blok_atas_tengah = Frame(blok_atas, width = (900/3) + 200, height = 800/2, border = 1, relief = RIDGE)
blok_atas_tengah.grid(row = 0, column = 1)
blok_atas_tengah.grid_propagate(False)

layar = Text(blok_atas_tengah, width = 42, height = 16, border = 5, relief = RIDGE, bg = "blue", fg = "white", font=("Consolas", 15))
layar.place(relx = 0.5, rely = 0.5, anchor="center")
layar.grid_propagate(0)

simbol1 = PhotoImage(file = ".\\simbol\\atmone.png")
tombol1 = Button(blok_bawah_tengah, border=4, image=simbol1, command = lambda: input_(1))
tombol1.place(width = 120, height =90, relx = 0.125, rely = 0.125, anchor="center")

simbol2 = PhotoImage(file = ".\\simbol\\atmtwo.png")
tombol2 = Button(blok_bawah_tengah, border=4, image = simbol2, command = lambda: input_(2))
tombol2.place(width = 120, height =90, relx = 0.375, rely = 0.125, anchor="center")

simbol3 = PhotoImage(file = ".\\simbol\\atmthree.png")
tombol3= Button(blok_bawah_tengah, border=4, image = simbol3, command = lambda: input_(3))
tombol3.place(width = 120, height =90, relx = 0.625, rely = 0.125, anchor="center")

simbolcancel = PhotoImage(file = ".\\simbol\\atmcancel.png")
tombol_cancel = Button(blok_bawah_tengah, border=4, bg = "red" , activebackground="red", image = simbolcancel, command=restart)
tombol_cancel.place(width = 120, height =90, relx = 0.875, rely = 0.125, anchor="center")

simbol4 = PhotoImage(file = ".\\simbol\\atmfour.png")
tombol4 = Button(blok_bawah_tengah, border=4, image=simbol4, command = lambda: input_(4))
tombol4.place(width = 120, height =90, relx = 0.125, rely = 0.375, anchor="center")

simbol5 = PhotoImage(file = ".\\simbol\\atmfive.png")
tombol5 = Button(blok_bawah_tengah, border=4, image = simbol5, command = lambda: input_(5))
tombol5.place(width = 120, height =90, relx = 0.375, rely = 0.375, anchor="center")

simbol6 = PhotoImage(file = ".\\simbol\\atmsix.png")
tombol6= Button(blok_bawah_tengah, border=4, image = simbol6, command = lambda: input_(6))
tombol6.place(width = 120, height =90, relx = 0.625, rely = 0.375, anchor="center")

simbolclear = PhotoImage(file = ".\\simbol\\atmclear.png")
tombol_clear = Button(blok_bawah_tengah, border=4, bg = "yellow" , activebackground="yellow", image = simbolclear, command=input_clear)
tombol_clear.place(width = 120, height =90, relx = 0.875, rely = 0.375, anchor="center")

simbol7 = PhotoImage(file = ".\\simbol\\atmseven.png")
tombol7 = Button(blok_bawah_tengah, border=4, image=simbol7, command = lambda: input_(7))
tombol7.place(width = 120, height =90, relx = 0.125, rely = 0.625, anchor="center")

simbol8 = PhotoImage(file = ".\\simbol\\atmeight.png")
tombol8 = Button(blok_bawah_tengah, border=4, image = simbol8, command = lambda: input_(8))
tombol8.place(width = 120, height =90, relx = 0.375, rely = 0.625, anchor="center")

simbol9 = PhotoImage(file = ".\\simbol\\atmnine.png")
tombol9= Button(blok_bawah_tengah, border=4, image = simbol9, command = lambda: input_(9))
tombol9.place(width = 120, height =90, relx = 0.625, rely = 0.625, anchor="center")

simbolenter = PhotoImage(file = ".\\simbol\\atmenter.png")
tombol_enter = Button(blok_bawah_tengah, border=4, bg = "green" , activebackground="green", image = simbolenter, command=input_enter)
tombol_enter.place(width = 120, height =90, relx = 0.875, rely = 0.625, anchor="center")

tombolkosong1 = Button(blok_bawah_tengah, border=4)
tombolkosong1.place(width = 120, height =90, relx = 0.125, rely =0.875, anchor="center")

simbol0 = PhotoImage(file = ".\\simbol\\atmzero.png")
tombol0 = Button(blok_bawah_tengah, border=4, image = simbol0, command = lambda: input_(0))
tombol0.place(width = 120, height =90, relx = 0.375, rely =0.875, anchor="center")

tombolkosong2= Button(blok_bawah_tengah, border=4)
tombolkosong2.place(width = 120, height =90, relx = 0.625, rely =0.875, anchor="center")

tombol_kosong3 = Button(blok_bawah_tengah, border=4)
tombol_kosong3.place(width = 120, height =90, relx = 0.875, rely =0.875, anchor="center")

state = "ID"
id = ""
# layar.delete('1.0', END) # Ekuivalen dengan os.system('cls')
layar.insert(END, "Masukkan nomor rekening Anda\nEnter your account number\n\n")
window.mainloop()