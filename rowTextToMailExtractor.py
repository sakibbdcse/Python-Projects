e = input("Enter Row text Extract to Email: ")
newtext = list(e.split())
for i in newtext:
    if ".com" in i:
        print(i)