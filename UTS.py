import json
import time 
import os 

Pernyataan = "Balasan.json"

def clean():
    os.system('cls')

def read():
    try :
        with open (Pernyataan , 'r') as DataTampilan:
            cekdata = json.load(DataTampilan)
        return cekdata
    except FileNotFoundError:
        Isidata = []
        with open (Pernyataan , 'w') as DataTampilan:
            json.dump(Isidata , DataTampilan , indent = 4)
        return Isidata

def write(cekdata): 
    with open (Pernyataan , 'w') as DataTampilan:
        json.dump(cekdata , DataTampilan , indent= 4)

def dataeaa():
    clean()

    choice1 = input("Who Are U : ")
    userdata = read()

    print("Hello , namaku Dejan")
    time.sleep(1)
    clean()
    terserahMauBukaApa()

def pilihan1():
    clean()
    print ("Hii, disini Aku hanya membuat program sederhana untuk mengirimkan suatu pesan yang diharapkan bisa dibaca oleh Anda")
   
    pil1 = input("Ada feedback : ")
    Jawaban = read()
    Data = {
        "Feedback" : pil1
    }

    Jawaban.append(Data)
    write(Jawaban)
    print("Thanks")
    time.sleep(1.5)
    clean()
    terserahMauBukaApa()


def Log_out():
    clean()
    print("Terima kasih banyak dah buka")
    print("Feedback bisa dikirimkan ke saya wkwkwkwk")


def terserahMauBukaApa():

    print(" Ini hanya program \n\n============ MENU ============\n\n   [1] Pesan\n   [2] Bisa keluar kok\n ")
    pilih = int(input("\n>> Pilih yang mana  : "))
    if pilih == 1:
        pilihan1()
    elif pilih == 2:
        Log_out()
    else:
        print('Menu yang anda masukan tidak tersedia!')
        time.sleep(1)
        clean()
        terserahMauBukaApa()

dataeaa()


