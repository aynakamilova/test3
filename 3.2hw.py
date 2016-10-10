x = int(input('введите число '))
for i in range(x,0,-1):
    for j in range(0,x):
        print(i+j,end=' ')
    print()
