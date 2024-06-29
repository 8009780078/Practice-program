'''str = input("enter any string name :  ")

print(len(str))
print(str.count("a"))
'''

'''
number = int(input("enter any number :  "))

if(number%2==0):
    print("even")

else:
    print("odd")'''

num1 = int(input("enter first number :  "))
num2 = int(input("enter second number :  "))
num3 = int(input("enter third number :  "))

if(num1>=num2 and num1>=num3):
    print(num1)
elif(num2>=num3):
    print(num2)
else:
    print(num3)
