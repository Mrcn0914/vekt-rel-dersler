
import turtle

print("Merhaba hangi şekil çizmek istersin?")
print("╔══════════════════════╗")
print("║      OYUNLAR         ║")
print("║  1.Kare              ║")
print("║  2.Ücgen             ║")
print("║  3.Daire             ║")
print("║  4.Altıgen           ║")
print("║  5.Dikdörtgen        ║")
print("║  6.Çiçek             ║")
print("║                      ║")
print("║                      ║")
print("║                      ║")
print("╚══════════════════════╝")

secim=input("Seciminizi yapın! (1 -7):" )
t=turtle.Turtle()
t.speed(20)


if secim=="1":
    for i in range(4):
        t.forward(100)
        t.left(90)   
elif secim=="2":
    for i in range(3):
        t.forward(100)
        t.left(120)   
elif secim=="3":
    t.circle(100)  
elif secim=="4":
    for i in range(6):
        t.forward(100)
        t.left(60)
elif secim=="5":
    for i in range(2):
        t.forward(150)
        t.left(90)
        t.forward(80)
        t.left(90)   
elif secim=="6":
    for i in range(36):
        t.circle(60)
        t.left(10)
turtle.done()                        
                

