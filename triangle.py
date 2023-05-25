def triangle(n):
    k = n-1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k-1
        for j in range(0, i+1):
            if j == min(range(0, i+1)):
                print("1 ", end="")
            elif j == max(range(0, i+1)):
                print("1 ", end="")
            else:
                print("  ", end="")
        print("\r")


def trianglerev(n):
    k = 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k+1
        for j in range(0, n-(i+1)):
            if j == min(range(0, n-(i+1))):
                print("1 ", end="")
            elif j == max(range(0, n-(i+1))):
                print("1 ", end="")
            else:
                print("  ", end="")
        print("\r")


n = int(input())
triangle(n)

trianglerev(n)
