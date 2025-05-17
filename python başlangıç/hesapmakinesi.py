def hesapmakinesi():
    while True:

        print("\033[1;35;47m")# Renkli yazmak için
        print("╔══════════════════════╗")
        print("║     Hesap Makinesi   ║")
        print("║  1.Toplama için +    ║")
        print("║  2.Çıkarma için -    ║")
        print("║  3.Çarpma için *     ║")
        print("║  4.Bölme için /      ║")
        print("║                      ║")
        print("║  Seciminiz nedir?    ║")
        print("╚══════════════════════╝")

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
                return
        else:
            print("Geçersiz işlem!")
            return
        print("Sonuç:",sonuc)

        tekrar=input("Yeni bir işlem yapmak istermisin? (e/h):").lower
        if tekrar !="h":
            print("Programdan çıkılıyor...")
            break

hesapmakinesi()
