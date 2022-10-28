from tkinter import *

# User Interface
window = Tk()
window.title(" " * 128 + "ATM BNI")
window.geometry("900x800+300+20")
window.minsize(900, 800)
window.maxsize(900, 800)

main = Frame(window, width = 900, height = 800, bg = "grey")
main.grid(row = 0, column = 0)

def input1():
    layar.insert(END, "1")

def input2():
    layar.insert(END, "2")

def input3():
    layar.insert(END, "3")

def input4():
    layar.insert(END, "4")

def input5():
    layar.insert(END, "5")

def input6():
    layar.insert(END, "6")

def input7():
    layar.insert(END, "7")

def input8():
    layar.insert(END, "8")

def input9():
    layar.insert(END, "9")

def input0():
    layar.insert(END, "0")

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
layar.configure(font=("Helvetica", 15))

simbol1 = PhotoImage(file = "atmone.png")
tombol1 = Button(blok_bawah_tengah, border=4, image=simbol1, command = input1)
tombol1.place(width = 120, height =90, relx = 0.125, rely = 0.125, anchor="center")

simbol2 = PhotoImage(file = "atmtwo.png")
tombol2 = Button(blok_bawah_tengah, border=4, image = simbol2, command = input2)
tombol2.place(width = 120, height =90, relx = 0.375, rely = 0.125, anchor="center")

simbol3 = PhotoImage(file = "atmthree.png")
tombol3= Button(blok_bawah_tengah, border=4, image = simbol3, command = input3)
tombol3.place(width = 120, height =90, relx = 0.625, rely = 0.125, anchor="center")

simbolcancel = PhotoImage(file = "atmcancel.png")
tombol_cancel = Button(blok_bawah_tengah, border=4, bg = "red" , activebackground="red", image = simbolcancel)
tombol_cancel.place(width = 120, height =90, relx = 0.875, rely = 0.125, anchor="center")

simbol4 = PhotoImage(file = "atmfour.png")
tombol4 = Button(blok_bawah_tengah, border=4, image=simbol4, command = input4)
tombol4.place(width = 120, height =90, relx = 0.125, rely = 0.375, anchor="center")

simbol5 = PhotoImage(file = "atmfive.png")
tombol5 = Button(blok_bawah_tengah, border=4, image = simbol5, command = input5)
tombol5.place(width = 120, height =90, relx = 0.375, rely = 0.375, anchor="center")

simbol6 = PhotoImage(file = "atmsix.png")
tombol6= Button(blok_bawah_tengah, border=4, image = simbol6, command = input6)
tombol6.place(width = 120, height =90, relx = 0.625, rely = 0.375, anchor="center")

simbolclear = PhotoImage(file = "atmclear.png")
tombol_clear = Button(blok_bawah_tengah, border=4, bg = "yellow" , activebackground="yellow", image = simbolclear)
tombol_clear.place(width = 120, height =90, relx = 0.875, rely = 0.375, anchor="center")

simbol7 = PhotoImage(file = "atmseven.png")
tombol7 = Button(blok_bawah_tengah, border=4, image=simbol7, command = input7)
tombol7.place(width = 120, height =90, relx = 0.125, rely = 0.625, anchor="center")

simbol8 = PhotoImage(file = "atmeight.png")
tombol8 = Button(blok_bawah_tengah, border=4, image = simbol8, command = input8)
tombol8.place(width = 120, height =90, relx = 0.375, rely = 0.625, anchor="center")

simbol9 = PhotoImage(file = "atmnine.png")
tombol9= Button(blok_bawah_tengah, border=4, image = simbol9, command = input9)
tombol9.place(width = 120, height =90, relx = 0.625, rely = 0.625, anchor="center")

simbolenter = PhotoImage(file = "atmenter.png")
tombol_enter = Button(blok_bawah_tengah, border=4, bg = "green" , activebackground="green", image = simbolenter)
tombol_enter.place(width = 120, height =90, relx = 0.875, rely = 0.625, anchor="center")

tombolkosong1 = Button(blok_bawah_tengah, border=4)
tombolkosong1.place(width = 120, height =90, relx = 0.125, rely =0.875, anchor="center")

simbol0 = PhotoImage(file = "atmzero.png")
tombol0 = Button(blok_bawah_tengah, border=4, image = simbol0, command = input0)
tombol0.place(width = 120, height =90, relx = 0.375, rely =0.875, anchor="center")

tombolkosong2= Button(blok_bawah_tengah, border=4)
tombolkosong2.place(width = 120, height =90, relx = 0.625, rely =0.875, anchor="center")

tombol_kosong3 = Button(blok_bawah_tengah, border=4)
tombol_kosong3.place(width = 120, height =90, relx = 0.875, rely =0.875, anchor="center")

window.mainloop()