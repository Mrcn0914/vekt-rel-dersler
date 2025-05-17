#ruh halini gösteren oyun
def ruh_hali_oyunu():
    
    print("Ruh Halini Söyle, Tepkimi Gör!")
    print("Nasıl hissediyorsun?")
    print("1 - Mutlu ")
    print("2 - Üzgün ")
    print("3 - Kızgın ")
    print("4 - Heyecanlı ")
    print("5 - Sıkılmış ")

    secim = input("Bir sayı gir (1-5): ")

    if secim == '1':
        print("Harika! Mutluluğun bulaşıcı! ")
    elif secim == '2':
        print("Üzülme, her şey geçer, biraz yürüyüş iyi gelir.. ")
    elif secim == '3':
        print("Derin bir nefes al... Her şey yoluna girecek ")
    elif secim == '4':
        print("Enerjin bize de geçti! ")
    elif secim == '5':
        print("Hadi biraz eğlence zamanı! ")
    else:
        print("Hmm, seni anlayamadım ama buradayım!")