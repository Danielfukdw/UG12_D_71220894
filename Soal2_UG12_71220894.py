#Test Case1
print ("Pilihan Model Matematika" "\n")
print ("1. Perkalian ")
print ("2. Pembagian")
case = int(input("Masukan Model Matematika yang di inginkan 1/2:"))
if case == 1:
    kali =(input("Masukan Table Matematika dari angka:"))
elif case == 2:
    bagi =(input("Masukan Table Matematika dari angka: "))
else :
    print ("Pilihan Tidak ada")
for i in range (1,11):
    print (kali,"x",i,"=",kali *i)
for i in range (1,11):
    print (bagi,":",i,"=",bagi/i)