#  Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
principalAmount = float(input("Enter Principal Amount: "))
interestAmount = float(input("Enter Interest of Amount: "))
time = int(input("Enter Time Period: "))

calculate_interest = (principalAmount*interestAmount*time)/100
print(calculate_interest)
total_deu = principalAmount+calculate_interest
print(f"total amount of deu you will be pray {total_deu}")
