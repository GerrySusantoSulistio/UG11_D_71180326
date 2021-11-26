def insertkarakter(kalimat,karakter):
    return kalimat.replace(''," "+karakter+" ")
def insertkata(kalimat,karakter):
    return kalimat.replace(' '," "+karakter+" ")

kalimat = input("Masukan sebuah kata/kalimat :")
karakter = input("Masukan karakter yang ingin disisipkan : ")

print(insertkarakter(kalimat,karakter))
print(insertkata(kalimat,karakter))