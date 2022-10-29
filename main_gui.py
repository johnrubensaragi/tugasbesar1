from tkinter import *
from hashlib import sha256
import os
import datetime
import pwinput
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

# nama bank
nama_bank = {"009" : "BNI",  "002" : "BRI", "008" : "MANDIRI", "011" : "DANAMON", "013" : "PERMATA", "014" : "BCA",
 		    "016" : "MAYBANK", "019" : "BANK PANIN", "022" : "CIMB NIAGA", "028" : "OCB NISP", "031" : "CITIBANK",
            "036" : "CCBINDONESIA", "037" : "ARTHA GRAHA", "046" : "BANK DBS", "050" : "STANCHART", "054" : "BANK CAPITAL",
            "061" : "ANZ", "200" : "BTN"}

# kamus untuk terjemahan
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
    layar.insert(END, tr("Masukkan PIN: "))
    pin = ""
    state = "PIN"

def penarikan_tunai():
    global state, last_state
    if (nominal % 5000000) == 0 and nominal > 0:
        if nominal <= balances_list[indeks]:
            if pin_sha256 == pin_list[indeks]:
                balances_list[indeks] -= nominal
                layar.delete('1.0', END)
                layar.insert(END, f"{tr('Penarikan berhasil dilakukan.')}\n")
                layar.insert(END, f"{tr('Saldo Anda sekarang adalah')}\n")
                layar.insert(END, f"Rp {ubah_format(str(balances_list[indeks]))}\n\n")
                balances_file.seek(0)
                for i in balances_list:
                    balances_file.writelines(str(i) + "\n")
                balances_file.truncate()
                state = "resi"
                layar.insert(END, f"{tr('Apakah Anda ingin mencetak resi?: ')}\n")
                layar.insert(END, f"{tr('1. Ya')}\n")
                layar.insert(END, f"{tr('2. Tidak')}\n")
            else:
                last_state = "penarikan_tunai"
                PIN_trial()
        else:
            print(tr("Maaf, saldo Anda tidak mencukupi."))
            time.sleep(5)
            state = "main1"
    else:
        print(tr("Transaksi tidak dapat diproses."))
        time.sleep(5)
        state = "main1"

# User Interface part 2
def update_trial_list():
    global percobaan, trial_list, trial_file
    trial_list[indeks] = str(percobaan)
    trial_file.seek(0)
    for i in trial_list:
        trial_file.writelines(i + "\n")
    trial_file.truncate()

def input_(num):
    global state, id, pin, pin_sha256, bahasa, wrongPIN, percobaan, nominal
    print(state)
    if state == "ID":
        id += str(num)
        layar.insert(END, str(num))
    elif state == "Bahasa" and (num == 1 or num == 2):
        bahasa = str(num)
        state = "PIN"
        layar.delete('1.0', END) # Ekuivalen dengan os.system('cls')
        wrongPIN = False
        layar.insert(END, tr("Masukkan PIN: "))
        pin = ""
    elif state == "PIN":
        if len(pin) < 6:
            pin += str(num)
            layar.insert(END, "X")
            if len(pin) == 6:
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
                        layar.insert(END, f"{tr('Anda sudah memasukkan PIN yang salah sebanyak 3 (tiga) kali.')}\n")
                        layar.insert(END, f"{tr('Akun Anda terblokir.')}\n")
                        time.sleep(5)
                        restart()
    elif state == "main1":
        if num == 1:
            nominal = 25000000
            penarikan_tunai()
        elif num == 2:
            nominal = 50000000
            penarikan_tunai()
        elif num == 3:
            nominal = 100000000
            penarikan_tunai()
        elif num == 4:
            nominal = 125000000
            penarikan_tunai()
        elif num == 5:
            state = "main2"
    elif state == "resi":
        if num == 1:
            #os.system('cls')
            #Receipt keluar dengan format : tanggal, waktu, dan lokasi ATM, jumlah penarikan, dan sisa saldo
            #print("-"*16, "Bank BNI", "-"*16)
            #print("TANGGAL " + " "*28 + " WAKTU")
            #print(waktu.strftime("%d/%m/%y"+ " "*29 +"%H:%M"))
            #print("PENARIKAN:" + " "*6 + f"Rp {ubah_format(str(nominal))}" )
            #print("SALDO REKENING:" + f" Rp {ubah_format(str(balances_list[indeks]))}")
            #print("-"*42)
            #input()
            time.sleep(10)
        state = "ganti pin?"
        layar.insert(END, f"{tr('Apakah Anda ingin mengganti PIN?: ')}\n")
        layar.insert(END, f"{tr('1. Ya ')}\n")
        layar.insert(END, f"{tr('2. Tidak ')}\n")
    elif state == "ganti pin?":
        #ganti_pin()
        state = "main1"
        layar.insert(END, f"{tr('Menu penarikan cepat')}\n1. Rp250.000,00\n2. Rp500.000,00\n3. Rp1.000.000,00\n4. Rp1.250.000,00\n{tr('5. Menu lain')}")
    else:
        state = "main1"
        layar.insert(END, f"{tr('Menu penarikan cepat')}\n1. Rp250.000,00\n2. Rp500.000,00\n3. Rp1.000.000,00\n4. Rp1.250.000,00\n{tr('5. Menu lain')}")

def restart():
    state = "main1"
    layar.insert(END, f"{tr('Menu penarikan cepat')}\n1. Rp250.000,00\n2. Rp500.000,00\n3. Rp1.000.000,00\n4. Rp1.250.000,00\n{tr('5. Menu lain')}")

def input_clear():
    global state, pin, id
    if state == "PIN":
        layar.delete(f"end-{len(pin)+1}c", END)
        pin = ""
    if state == "ID":
        layar.delete(f"end-{len(id)+1}c", END)
        layar.insert(END, "\n")
        id = ""

def input_enter():
    global state, id, indeks
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

layar = Text(blok_atas_tengah, width = 42, height = 16, border = 5, relief = RIDGE)
layar.place(relx = 0.5, rely = 0.5, anchor="center")
layar.grid_propagate(0)
layar.configure(font=("Consolas", 15))

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
tombol_cancel = Button(blok_bawah_tengah, border=4, bg = "red" , activebackground="red", image = simbolcancel, command=lambda:restart())
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
layar.insert(END,"Masukkan nomor rekening Anda\nEnter your account number\n\n")
window.mainloop()