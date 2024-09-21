#Jika blok try error/salah maka blok except akan diesekusi (error: x tidak terdefinisikan)
try:
    print(x)
except:
    print("Exception dijalankan")

print("==================")
#jika tidak ada error maka eksekusi blok else
try:
    print("Halo Python")
except:
    print("Ada error")
else:
    print("Tidak ada error")

print("==================")
# blok finally akan tetap dieksekusi meskipun terjadi error ataupun tidak
try:
    print(x)
except:
    print("Ada error")
finally:
    print("Program Selesai")