sayac = 0
sayi = int(input("Sayı: "))
while(True):
    if sayi == 1:
        print(sayi, "Asal değildir.")
        break
    for i in range(2,sayi):
        if sayi % i ==0:
            sayac+=1
            break
    if sayac!=0:
        print(sayi, "Asal değil.")
        break
    else:
        print(sayi, "Asal sayıdır.")
        break
