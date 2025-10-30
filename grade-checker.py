marks = int(input("Enter the Score: "))

if marks >= 90:
    print("Grade : A")
elif 80 <= marks <= 89:
    print("Grade : B")
elif 70 <= marks <= 79:
    print("Grade : C")
elif 60 <= marks <= 69:
    print("Grade : D")
else:
    print("Grade : F")