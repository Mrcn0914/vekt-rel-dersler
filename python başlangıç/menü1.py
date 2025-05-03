print("menü1 içeriği")


def anamenü():
    
    print("║      OYUNLAR         ║")
    print("║  1.TETRİS            ║")
    print("║  2.BULMACA           ║")
    print("║  3.HARF BULMACA      ║")
    print("║  4.ZAR ATMA          ║")
    print("║  5.YILAN OYUNU       ║")
    print("║  6.QUİZ OYUNU        ║")
    print("║  7.BASİT MATEMATİK   ║")
    print("║                      ║")
    print("║ Seçiminiz nedir?     ║")
    print("╚══════════════════════╝")

    secim = input()
    if secim =="1" :
        import TETRİS
    anamenü()
anamenü()

   

