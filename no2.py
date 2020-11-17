a = input("Klub A : ")
b = input('Klub B : ')
x = 0
n = 0
skor = []
while x >= 0:
    n += 1
    c,d = input(f"Pertandingan {n}: ").split()
    if int(c) >= 0 and int(d) >= 0:
        skor.append([c,d])
    else:
        break

for i in range(1,n):
    if int(skor[i-1][0]) > int(skor[i-1][1]):
        print(f"Hasil {i}: {a}")
    elif int(skor[i-1][0]) < int(skor[i-1][1]):
        print(f"Hasil {i}: {b}")
    elif int(skor[i-1][0]) == int(skor[i-1][1]):
        print(f"Hasil {i}: Draw")

print("Pertandingan selesai")