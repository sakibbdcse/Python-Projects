# Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

userInput = input("Enter The Number: ")
reversing = userInput[::-1]
separateing = " ".join(reversing)
print(separateing)
