
#for loop 1st form
no = int(input("Enter how many times you want to run the loop "))
for i in range(0,no):
    print(i)

#for loop 2nd form
list1 = ["item1","item2","item3"]
for item in list1:
    print(item)

#nested for loop
list1 = [[1,2,3],[4,5,6],[7,8,9]]
for item in list1:
    for i in item:
        print(i)

#nested item in a list
print(list1[0][0])

#while loop
#continue means niche saare line chodke baaki execute karo
#break means come out of the loop when a specific condition is met
print("Enter a number ")
number=int(input())
while(number>4):
    print("Number is greater than 4")
    number=int(input())
    if(number==9):
        break
    if(number==8):
        continue
    print("loop ended")
