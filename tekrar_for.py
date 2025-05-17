for a in range(1,11):
    #if a>5 : break # bitiriyor
    if a % 2 == 0:continue # döngünün sonuna atlama
    for b in range(1,11):
        if b & 2==1:continue
        print(f"{a}*{b}={a*b}")
    print()
    


