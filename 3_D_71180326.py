import random
tipe = input("Masukan tipe yang ingin anda coba :")
tipe = tipe.lower()
perbandingan=['<','>','==']
def generateSoal():
    nomor1=random.randint(1,20)
    nomor2=random.randint(1,20)
    nomor3=random.randint(1,20)
    nomor4=random.randint(1,20)
    banding =random.choice(perbandingan)
    if(tipe == "penjumlahan" ):
        total1=nomor1+nomor2
        total2=nomor3+nomor4
        print("(benar/salah) jika "+str(nomor1)+"+"+str(nomor2)+str(banding)+str(nomor3)+"+"+str(nomor4))
        cekHasil(total1,total2,banding)
    elif(tipe == "pengurangan" ):
        total1=nomor1-nomor2
        total2=nomor3-nomor4
        print("(benar/salah) jika %d+%d%d%d+%d",nomor1,nomor2,banding,nomor3,nomor4)
        banding1= eval(str(total1) + str(banding) + str(total2))
        cekHasil(total1,total2,banding)
    else:
        return 0
        

def cekHasil(total1,total2,banding):
    banding1= eval(str(total1) + str(banding) + str(total2))
    jawab=input("Maskkan Jawaban Anda : ")
    jawab=jawab.lower()
    if(banding1 == True and jawab == "benar"):
        print("Jawaban Anda Benar !")
    elif(banding1 == False and jawab == "salah"):
        print("Jawaban Anda Benar !")
    else:
        print("Jawaban Anda Masih Salah !")
generateSoal()
