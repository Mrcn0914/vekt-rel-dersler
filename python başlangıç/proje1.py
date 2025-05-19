def anaekran():
    while True:
        print("\033[1;32;40m")# Renkli yazmak için
        print("╔══════════════════════╗")
        print("║     Proje Listesi    ║")
        print("║  1.Hesap Makinesi    ║")
        print("║  2.Tahmin Oyunu      ║")
        print("║  3.Vki Hesaplama     ║")
        print("║  4.Kur Dönüstürücü   ║")
        print("║  5.Puan Hesaplama    ║")
        print("║  6.Ruh Halini Söyle  ║")
        print("║  7.Geometrik Şekiller║")
        print("║                      ║")
        print("║ Seciminiz nedir?     ║")
        print("╚══════════════════════╝")

        secim = input("Seçiminizi girin (1-7): ")

        if secim == "1":
            import hesapmakinesı
            hesapmakinesı.hmmenu()
        elif secim == "2":
            import tahminoyunu
            tahminoyunu.tahmin_et()
        elif secim == "3":
            import vki_hesaplama
            vki_hesaplama.vkıhesap()
        elif secim =="4":
            import kurhesaplama
            kurhesaplama.kurmenu()
        elif secim =="5" :
            import puanhesapla
            puanhesapla.puanmenu()
    
        elif secim =="6" :
            import ruhhalinisoyle
            ruhhalinisoyle.ruh_hali_oyunu()
        elif secim =="7":
            import geometrıksekıller
            geometrıksekıller.geometrıkmenu()
        elif secim == "0":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-7 arasında bir seçim yapın.")

        input("\nDevam etmek için Enter'a basın...")
        anaekran()
    
anaekran()