sm= input("Enter parttern symbol: ")
n = int(input("Enter parttern symbol: "))
for i in range(1,n+1):
    for j in range(0,i):
        print(sm, end=" ")
    print("\n")