# Check file is empty or not,Write a program to check if the given file is empty or not
import os
filePath = "./upload/test.txt"
size = os.stat(filePath).st_size
if size==0:
    print("file is empty")
else:
    print("file is not empty")