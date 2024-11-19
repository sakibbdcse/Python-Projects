print('----- Gussing Game -------')
print("input [x] for exist")
while True:
    inp =input("Tall Me a Numbar: ")
    if inp == 'x':
        break
    try:
        number = float(inp)
    except ValueError:
        print("I said: Tall me a Numbar...!!")
    else:
        test = number % 2
        if test == 0:
            print(int(number),"Number is Even")
        elif test == 1:
            print(int(number),"Number is Odd")
        else:
            print(int(number),"Number is very Strange..!!")
