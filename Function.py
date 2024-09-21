# fungsi sederhana
def fungsihalo():
    print("halo dunia")
    fungsihalo()

print("=====================")
#fungsi dengan 1 argumen
def my_function(namadepan):
    print(namadepan + " Prasetyo")

my_function("Andi")
my_function("Boim")
my_function("Cici")

print("======================")
#fungsi dengan lebih dari 1 argumen
def my_function(namadepan, namabelakang):
    print(namadepan + "Dedi " + namabelakang)

my_function("Andi", "Prasetyo")

print("=======================")
#fungsi dengan jumlah argumen yg belum ditentukan
def my_function(*anak):
    print("Anak pertama saya adalah " + anak [2])

my_function("Andi", "Boim", "Cici")

print("========================")
#fungsi dengan nilai return
def my_function(x):
    return 5 * x
print(my_function(2))
print(my_function(4))