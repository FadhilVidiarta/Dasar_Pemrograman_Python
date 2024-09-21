# While Loop
i = 1
while i < 10:
    print(i)
    i += 1

print("=====================")
# Break pada loop
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

print("=====================")
# Continue pada loop
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

print("=====================")
# While dengan else
i = 1
while i < 10:
    print(i)
    i += 1
else:
    print("stop iterasi, i harus kurang dari 10")