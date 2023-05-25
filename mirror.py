num = int(input())
for i in range(1, num+1):
    for i in range(0, i):
        print("*", end=" ")
    print("")


for i in range(1, num+1):
    for i in range(0, num-i):
        print("*", end=" ")
    print("")
