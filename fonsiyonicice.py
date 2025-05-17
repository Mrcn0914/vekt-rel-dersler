def hesapla (a,b,c):
    def topla(a,b):
        print("toplam:",a+b)

    def carp(x,y):
        print("carpımı:",x*y)

    if c=="+":topla(a,b)
    elif c=="*":carp(a,b)

hesapla(4,5,"*")