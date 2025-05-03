print("Evet şimdi zihnini okuacağım!Aklından bir hayvn tut.(Ama söyleme!)")
print("Birkaç soru soracağım ve ne olduğunu bulmaya çalışcağım.")
input("Hazırmısın? Entera bas ve başlayalım...")

cevap1=input("Uçabiliyor mu? (evet\hayır):").lower()
cevap2=input("Suda yaşıyor mu? (evet\hayır):").lower()
cevap3=input("Sürüngen mi? (evet\hayır):").lower()

print("Tahmin ediyorum biraz beklermisin?")

if cevap1=="evet":
    if cevap2=="evet":
        print("Aklındaki hayvan...tavuk mu?")
    else:
        print("Aklındaki hayvan kuş mu?")
elif cevap2=="evet":
    print("Aklındaki hayvan....balık mı?")
elif cevap3=="evet":
    print("Aklındaki hayvan köpek mi?")
else:
    print("Aklındaki hayvan....bir yılan mı?")
