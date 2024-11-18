# try:
#     age = int(input("age: "))
#     print(f"your age is {age}")
# except ValueError:
#     print('Invalid Value')

#Zero Division Error Handling 
try:
    age = int(input("age: "))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("Age can not be Zero")
except ValueError:
    print("Invalid value")