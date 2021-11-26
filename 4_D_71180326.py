import random
mulai = input("Untuk memulai program masukan (-1) untuk memulai \n :")

def tebakangka(angka,idx):
    if(idx==1): 
        print("Apakah "+str(angka)+" ?")
        print("Apakah tebakan sudah benar ?")
        print("lebih kecil (0)")
        print("lebih besar (1)")
        print("benar (2) ")
        jawab=input(": ")
        if(angka == 0 and int(jawab) == 0):
            angka=angka
        elif(angka == 4 and int(jawab) == 1):
            angka=angka
        elif(int(jawab) == 0):
            angka=angka-random.randint(0+angka, 4)
        elif(int(jawab) == 1):
            angka=angka+random.randint(0, 4-angka)
        elif(int(jawab) == 2):
            angka=angka
        return angka
    if(idx==2):
        print("Apakah "+str(angka)+" ?")
        print("Jumlah tebakan :",idx)
        print("Apakah tebakan sudah benar ?")
        print("lebih kecil (0)")
        print("lebih besar (1)")
        print("benar (2) ")
        jawab=input(": ")
        if(angka == 0 and int(jawab) == 0):
            angka=angka
        elif(angka == 4 and int(jawab) == 1):
            angka=angka
        elif(int(jawab) == 0):
            angka=angka-random.randint(0+angka, 4)
        elif(int(jawab) == 1):
            angka=angka+random.randint(0, 4-angka)
        elif(int(jawab) == 2):
            angka=angka
        return angka
    elif(idx==3):
        print("Hasil Penjumlahan Pasti "+str(angka)+" !")
        print("Jumlah tebakan :",idx)
        print("Program selesai !")

angka=["",""]
if(mulai == "-1"):
    angka1=random.randint(0,4)
    angka[0]=tebakangka(angka1,1)
    angka2=random.randint(0,4)
    angka[1]=tebakangka(angka2,2)
    total=angka[0]+angka[1]
    tebakangka(total,3)
else:
    print("Program tidak berhasil dijalankan")
   