k=ord("A")
for i in range(4):
    for j in range(4-i):
        print(chr(k),end=" ")
        k=k+1
    print()