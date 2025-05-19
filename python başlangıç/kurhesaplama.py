def kurmenu():
    print("\033[1;34;40m")  # Renkli yazmak için
    print("╔══════════════════════╗")
    print("║    Kur Dönüştürücü   ║")
    print("║  1.TL'den USD        ║")
    print("║  2.TL'den EUR        ║")
    print("║  3.USD'den TL        ║")
    print("║  4.EUR'dan TL        ║")
    print("║                      ║")
    print("║  Seciminiz nedir?    ║")
    print("╚══════════════════════╝")

    secim = input("Seçiminizi yapın (1-4): ")
    if secim in ['1', '2', '3', '4']:
        miktar = float(input("Miktarı girin: "))
        if secim == '1':
            print(f"{miktar} TL = {miktar / 32:.2f} USD")
        elif secim == '2':
            print(f"{miktar} TL = {miktar / 35:.2f} EUR")
        elif secim == '3':
            print(f"{miktar} USD = {miktar * 32:.2f} TL")
        elif secim == '4':
            print(f"{miktar} EUR = {miktar * 35:.2f} TL")
    else:
        print("Geçersiz seçim!")

if __name__ == "__main__":
    kurmenu()
    input("Çıkmak için Enter'a basın...")
