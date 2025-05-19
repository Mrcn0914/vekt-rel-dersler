def vkıhesap():
    #boy kilo hesaplaması
    boy=int(input("Boyunuzu metre cinsinden giriniz:"))
    kilo=int(input("Kilonuzu girin(kg):"))

    vki=kilo/(boy**2)

    print("Vücut Kitle İndeksiniz(VKİ):",vki )

    if vki<12.5:
        print("durum:,zayıf")
    elif 12.5<=vki<30:
        print("durum:,normal ideal")
    elif 25<=vki<30:
        print("durum:,fazla kilolu")
    else:
        print("Durum obez")
    
         
