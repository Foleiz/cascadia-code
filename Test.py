# Simple calculator to perform basic arithmetic operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Example usage
'''
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"The result is: {add(num1, num2)}")         # .format
    elif choice == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input")
'''
#     # BMI Calculation
# print("\nBMI Calculation:")
# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))
# bmi = weight / (height ** 2)
# bm1 = height **2
# print(f"Your BMI is: {bmi:.2f}")

# ---------------------------------------------------------------

# import datetime
# d = datetime.datetime.now()
# print(d)

# string = "HE-LL-O"
# for i in range(len(string)):
#     if string[i] == "-":
#         #continue   # ข้านเฉพาะรอบนี้
#         pass        # ข้ามเฉยๆ
#     else:
#         print(string[i] ,end="")


# string = "HE-LL-O"
# new_string = string.replace("-", "")
# print(new_string)

numbers = [4, 7, 12, 15, 20]
num = 0
for i in numbers:
    num += i
print(num)

num1 = []
num2 = []
for i in numbers:
    if i % 2 == 0:
        num1.append(i)
    else:
        num2.append(i)
print(f"เลขคุ่ = {num1}")
print(f"เลขคี่ = {num2}")   

fruits = ['apple', 'banana', 'cherry', 'date']
num3 = []
for i in range(len(fruits)-1,-1,-1):
    num3.append(fruits[i])
print(num3)

save = {}
for i in range(2):
    name = input("Enter name: ")
    save.append(name)
    print(save)
    

