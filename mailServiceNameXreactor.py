e = input("Enter Email: ")
emailList = []
emailList.append(e)
for i in emailList:
    i = i.replace("@",'.').split(".")
    print(i[1])