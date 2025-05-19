def hmmenu():

    print("Toplama için +")
    print("Çıkarma için -")
    print("Çarpma için *")
    print("Bölme için /")
    sayı1=float(input("Birinci sayıyı girin:"))
    islem=input("işlem seçin(+,-,*,/):")
    sayı2=float(input("İkinci sayıyı girin:"))

    if islem=="+":
        sonuc=sayı1+sayı2
    elif islem=="-":
        sonuc=sayı1-sayı2
    elif islem=="*":
        sonuc=sayı1*sayı2
    elif islem=="/":
        if sayı2 != 0:
            sonuc=sayı1/sayı2
        else:
            print("Sıfıra bölme hatası")

    else:
        print("Geçersiz işlem!")
    print("Sonuç:",sonuc)

