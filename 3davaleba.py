import random

while True:
    a = int(input("sheiyvanet shualedis pirveli ricxvi: "))
    b = int(input("sheiyvanet shualedis meore ricxvi: "))
    n = int(input("sheiyvanet raodenoba ricxvebis: "))
    set2 = set(random.sample(range(a, b + 1), k=n))
    set1 = set()
    while True:
        for i in range(0, n):
            set1.add(int(input("sheiyvanet unikaluri ricxvebi: ")))

        if len(set1) < n:
            print("tqven sheiyvanet ertnairi ricxvebi amitom tavidan scadet")
            for m in range(0, n - n):
                set1.add(int(input("sheiyvanet unikaluri ricxvebi: ")))
        if len(set1) == n:
            break

    print("compiuteris ricxvebi:")
    print(set2)
    print("tqveni ricxvebi:")
    print(set1)
    print("tqven gamoicanit", len(set1.intersection(set2)), "ricxvi:")
    print(set1.intersection(set2))
    user = input("gindat gagrdzeleba? ki/ara: " )
    if user == "ara":
        break


