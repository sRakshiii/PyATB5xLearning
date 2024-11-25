#create a program to sum of three number from the user input,
#if user doesn't enter any number, use default as 100, 200, 300

def sum_of_three(num1=100, num2=200, num3=300):
    print("sum of three number")
    return num1+num2+num3

num1 = int(input("num1 :"))
num2 = int(input("num2 :"))
num3 = int(input("num3 :"))

result = sum_of_three(num1,num2,num3)
print(result)
