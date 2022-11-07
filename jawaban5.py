print("Nama : Nazlha Noor Aiena Sofhie")
print("Nim : 20210801281")
print("Jurusan : Teknik Informatika")
print("===================================")
def pilihan():
    menuA = "capucino"
    menuB = "teh"
    print ("Pilihan")
    print ("1.", menuA)
    print ("2.", menuB)
    print ("3. Exit")
 
def capucino():
    bonjol = "memilih capucino"
    print(bonjol)
    capucino = int(input("masukkan harga : "))
    PPN = 10/100
    harga = capucino*PPN
    total = capucino+harga
    print("jumlah yang harus di bayar", total)
 
def teh():
    teh = "memilih TEH"
    print(teh)
    teh = int(input("masukkan harga : "))
    PPN = 10/100
    harga = teh*PPN
    total = teh+harga
    print("jumlah yang harus di bayar", total)
 
def data():
    NIM = "20210801281"
    NAMA = "NAZLHA NOOR AIENA SOFHIE"
    print ("NIM : ", NIM)
    print ("NAMA : ", NAMA)
 
while True:
    data()
    pilihan()
    a = int(input("masukkan pilihan : "))
    if a == 1:
        capucino()
    elif a == 2:
        teh()
    elif a == 3:
        break
    else:
        print ("pilihan tidak tersedia")
