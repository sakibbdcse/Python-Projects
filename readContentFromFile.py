import os
filePath = "./upload/test.txt"
with open(filePath) as f_obj:
    content = f_obj.read()
    print(content)
    # read line by line
    print("Read line by line")
    for line in f_obj:
        print(line.rstrip())
    

