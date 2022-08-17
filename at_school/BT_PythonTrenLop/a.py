a = []

n = int(input("Enter number: "))
for i in range(0, n):
    ele = int(input('Enter the element in array '))
    a.append(ele)

print(a)
for i in range(len(a)):
    print(len(a))
    x = a[i - 2]
    y = a[i - 1]
    z = a[i]
    print("i la {} x la {} y la {} z la {}".format(i, x, y, z))
    if x + y == z:
        print(x, y, z)
