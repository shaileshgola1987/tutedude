context = {"Niraj":"A","Rohit":"B"}
student = input(str("Enter the Student Name: "))
grade = input(str("Enter the Student Grade: "))

context.update({student:grade})

print(context)