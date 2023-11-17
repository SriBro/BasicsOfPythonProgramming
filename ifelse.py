number = int(input("Enter your marks "))

if(number>90 and number<=100):
    grade='A'
elif(number>80 and number<=90):
    grade='B'
elif(number>70 and number<=80):
    grade='C'
elif(number>60 and number<=70):
    grade='D'
elif(number>=0 and number<=60):
    grade='F'
else:
    grade = 'Invalid marks'

print(grade)