# for loop
makan = ["nasi pecel", "rawon", "soto ayam"]
for x in makan:
    print(x)

print("===================================")
#loop karakter pada string
for x in "Politeknik":
    print(x)

print("===================================")
# break pada for
buah = ["mangga", "pisang", "jambu"]
for x in buah:
    print(x)
    if x == "pisang":
        break

print("===================================")
# coutinue pada for
buah = ["mangga", "pisang", "jambu"]
for x in buah:
    if x == "pisang":
        continue
    print(x)

print("===================================")
# fungsi range
for x in range(10):
    print(x)

print("===================================")
#fungsi range menggunakan prameter start
for x in range(4, 10):
    print(x)

print("===================================")
# fungsi range dengan step 3
for x in range(4, 20, 3):
    print(x)

print("===================================")
# nested loop
buah = ["mangga", "pisang", "jambu"]
sifat = ["tua", "besar", "manis"]

for x in buah:
    for y in sifat:
        print(x,y)