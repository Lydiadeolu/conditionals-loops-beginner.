Grade_checker = int(input('Enter your score between 0 - 100:'))
if 70 <= Grade_checker <= 100 :
    print("A")
elif 60 <= Grade_checker <= 69:
    print("B")
elif 50 <= Grade_checker <= 59:
    print("C")
elif 40 <= Grade_checker <= 49:
    print("D")
elif 0 <= Grade_checker <= 39:
    print("F")
else:
    print("Try again")
    