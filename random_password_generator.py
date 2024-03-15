import random

secenekler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

tercih = int(input("kaç değerli bir parolanız olmasını istiyorsunuz? "))

for i in range(tercih):
    sifre = random.choice(secenekler)
    print(sifre)
