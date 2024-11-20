# Swap the number without using third varible
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
print(x,y)
x =x+y
y =x-y
x =x-y
print(x,y)
