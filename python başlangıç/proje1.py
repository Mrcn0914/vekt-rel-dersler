
print("\033[1;32;40m")# Renkli yazmak için
print("╔══════════════════════╗")
print("║     Proje Listesi    ║")
print("║  1.Hesap Makınası    ║")
print("║  2.Tahmin Oyunu      ║")
print("║  3.HARF BULMACA      ║")
print("║  4.ZAR ATMA          ║")
print("║  5.YILAN OYUNU       ║")
print("║  6.QUİZ OYUNU        ║")
print("║  7.BASİT MATEMATİK   ║")
print("║                      ║")
print("║ Seciminiz nedir?     ║")
print("╚══════════════════════╝")

secim = input()
if secim == "1" : print("Hesap makinesini seçtiniz")
if secim == "2" : print("Tahmin Oyunu seçtiniz")
if secim == "3" : print("Harf Bulmaca seçtiniz")

secim=input()
if secim =="1":print("Hesap Makinası seçtiniz\nBiraz calışma yapmaya ne dersin?")
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


secim=input()
if secim =="2":print("Tahmin Oyunu seçtiniz! Haydi biraz tahmin yürütelim")
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

if secim =="3":print("HARF BULMACA SECTİNİZ")
if secim =="4":print("ZAR ATMA")
if secim =="5":print("YILAN OYUNU")
if secim =="6":print("QUİZ OYUNU")
if secim =="7":print("BASİT MATEMATİK")

