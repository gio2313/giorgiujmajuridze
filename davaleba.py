def martivi_ricxvebi(num):
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i

gen = martivi_ricxvebi(10000000000)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
