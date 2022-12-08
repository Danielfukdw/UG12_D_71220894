#Test Case1
print ("Pilihan Model Matematika" "\n")
print ("1. Perkalian ")
print ("2. Pembagian")
case = int(input("Masukan Model Matematika yang di inginkan 1/2:"))
if case == 1:
    kali =(input("Masukan Table Matematika dari angka:"))
    for x in range (1,11):
        print(kali, "x", x ,"=", kali *= x )
        
elif case == 2:
    bagi =(input("Masukan Table Matematika dari angka: "))
    for x in range (1,11):
        print(bagi, ":", x, "=", bagi / 10)
else :
    print ("Pilihan Tidak ada")

