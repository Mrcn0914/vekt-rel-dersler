def tahmin_et():
      
    print("Evet, şimdi zihnini okuyacağım! Aklından bir hayvan tut. (Ama söyleme!)")
    print("Birkaç soru soracağım ve ne olduğunu bulmaya çalışacağım.")
    input("Hazır mısın? Enter'a bas ve başlayalım...")

    cevap1 = input("Uçabiliyor mu? (evet/hayır): ").lower()
    cevap2 = input("Suda yaşıyor mu? (evet/hayır): ").lower()
    cevap3 = input("Sürüngen mi? (evet/hayır): ").lower()
    print("Tahmin ediyorum... Biraz bekler misin?")

    if cevap1 == "evet":
        if cevap2 == "evet":
            print("Aklındaki hayvan... ördek olabilir mi?")
        else:
            print("Aklındaki hayvan... kuş olabilir!")
    elif cevap2 == "evet":
        print("Aklındaki hayvan... balık mı?")
    elif cevap3 == "evet":
        print("Aklındaki hayvan... yılan mı?")
    else:
        print("Hmm... belki bir kedi ya da köpek olabilir!")
