grade_checker = int(input('Enter your score between 0 - 100: '))

if 70 <= grade_checker <= 100 :
    print("A")
elif 60 <= grade_checker <= 69:
    print("B")
elif 50 <= grade_checker <= 59:
    print("C")
elif 40 <= grade_checker <= 49:
    print("D")
elif 0 <= grade_checker <= 39:
    print("F")
else:
    print("Try again")
    