# Menghasilkan Output berupa menu
print("Operasi Matematika")
print(" 1. Jumlah \t [+]")
print(" 2. Kurang \t [-]")
print(" 3. Kali \t [*]")
print(" 4. Pembagian \t [/]")
print ('=' * 25)

# Menghasilkan Output berupa inputan 
operasi = input('Pilih operasi (1/2/3/4) \t : ')
print ('=' * 25)
bilangan1 = 6
bilangan2 = 3


# Function untuk perhitungan mulai dari penambahan, pengurangan, pembagian, dan perkalian 
# Menggunakan tiga parameter yaitu operasi, bilangan1, dan bilangan2
def penambahan(operasi, bilangan1, bilangan2):
    if operasi == '1' :
        hasil = int(bilangan1) + int(bilangan2)
        print(f'Hasil dari {bilangan1} + {bilangan2} = ', hasil)
        return hasil

def pengurangan(operasi, bilangan1, bilangan2):
    if operasi == '2' :
        hasil = int(bilangan1) - int(bilangan2)
        print(f'Hasil dari {bilangan1} - {bilangan2} = {hasil}')
        return hasil

def perkalian(operasi, bilangan1, bilangan2):
    if operasi == '3' :
        hasil = int(bilangan1) * int(bilangan2)
        print(f'Hasil dari {bilangan1} * {bilangan2} = {hasil}')
        return hasil

def pembagian(operasi, bilangan1, bilangan2):
    if operasi == '4' :
        hasil = int(bilangan1) / int(bilangan2)
        print(f'Hasil dari {bilangan1} / {bilangan2} = {int(hasil)}')
        return hasil

def TidakAdaHasil(operasi):
        if operasi > '4' :
            hasil = print("Gak jelass")
            return hasil 

penambahan(operasi, bilangan1, bilangan2)
pengurangan(operasi, bilangan1, bilangan2)
perkalian(operasi, bilangan1, bilangan2)
pembagian(operasi, bilangan1, bilangan2)
TidakAdaHasil(operasi)