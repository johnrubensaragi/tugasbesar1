from hashlib import sha256
from getpass import getpass

def login():
    ID_data = open("id.txt", "r+")                              # r+ artinya read and write
    ID_per_line = [str(line).strip('\n') for line in ID_data]   # menggunakan fungsi strip() untuk membuang '\n'
    N = len(ID_per_line)                                        # menunjukkan jumlah data
    ID = input("Masukkan nomor rekening Anda: ")
    index = 0
    ID_match = ID_per_line[index] == ID                         # ID_match: menunjukkan apakah ID sudah benar atau salah
    while not ID_match:
        ID_match = ID_per_line[index] == ID
        if not ID_match:
            index += 1
        if index >= N:
            print(f"Nomor rekening {ID} tidak terdaftar.")
            ID = input("Masukkan nomor rekening Anda: ")
            index = 0
    PIN = getpass("Masukkan PIN anda: ")
    PIN_SHA256 = sha256(PIN.encode('utf-8')).hexdigest()
    PIN_SHA256_data = open("pin.txt", "r+")
    PIN_SHA256_per_line = [str(line).strip('\n') for line in PIN_SHA256_data]
    PIN_match = PIN_SHA256_per_line[index] == PIN_SHA256
    while not PIN_match:
        print("PIN anda salah.")
        PIN = input("Masukkan PIN Anda: ")
        PIN_SHA256 = sha256(PIN.encode('utf-8')).hexdigest()
        PIN_match = PIN_SHA256_per_line[index] == PIN_SHA256
    print("PIN benar.")
    ID_data.close()
    PIN_SHA256_data.close()
# MAIN
login()