def puanhesapla():
    print("Puan Hesaplama")
    print("*******************\n")

    try:
        puan = int(input("Notunuz kaç? "))

        if puan > 100:
            print("100'den büyük not giremezsiniz.")
        elif puan < 0:
            print("Negatif not olmaz.")
        elif puan >= 80:
            print("Çok iyisin! ")
            print("Geçtiniz tebrikler :)")
        elif puan >= 60:
            print("Geçtiniz tebrikler :)")
        else:
            print("Kaldınız. Daha çok çalışmalısınız :(")

    except ValueError:
        print("❌ Lütfen geçerli bir sayı girin.")

# Bu satır fonksiyonun doğru şekilde çağrılmasını sağlar
if __name__ == "__main__":
    puanhesapla()
