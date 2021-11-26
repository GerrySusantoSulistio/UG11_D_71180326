input1 = input("Masukkan string : ")

def string():
    hasil = input1 [::-1]
    print(hasil)

def digit():
    numint = float(input1)
    if (numint % 2) == 0:
        hasil = int(numint/2)
        print(hasil)
    else:
        hasil = int((numint+5)/2)
        print(hasil)

x = input1.isdigit()
if x == True:
    digit()
else:
    string()


    

