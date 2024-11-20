x = int(input("Enter Theree Number: "))

a = x%10 #get last disit of input
num = x//10 #get intiger divition find first tow disit
b = num%10 #get 2nd disit
c = num//10

sumOfThereNumber = a+b+c
print(sumOfThereNumber)