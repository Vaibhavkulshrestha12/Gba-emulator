"""
details = {
    "name": "Vaibhav",
    "age": 23,
    "city": "Orai"
}

print("Name:", details["name"])
print("Age:", details["age"])
print("city:", details["city"])
"""

'''
a =10
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)
'''

'''
username = input("Enter your name: ")
password = input("enter your password: ")
 
if username == "vaibhav" and password == "123":
    print("Welcome mere chaman")
else:
    print("bhag ja bsdk")'''

'''
number = int (input("Enter a number: "))

if number % 2 ==0 or  number % 5 == 0:
    print("success")
else:
    print("failed")
    
'''

'''
number =  int(input("Enter a number: "))
if 10 <= number <=20 and number != 15:
    print("success")
else:
    print("failed")

'''
'''
age = int(input("Enter your age: "))
creditscore = int(input("Enter your credit score: "))
salary = int(input("Enter your salary: "))

if  18 <= age <= 65 and creditscore >= 700 and salary > 30000 :
    print("you are eligible for loan")
else:
    print("you are not eligible for loan")
    
'''
"""
side1 = int(input("Enter side1: "))
side2 = int(input("Enter side2: "))
side3 = int(input("Enter side3: "))

if(side1 + side2 > side3) and (side1 + side3 >side2) and (side2 + side3 > side1):
    print("triangle is valid")
else:
    print("triangle is not valid")    
"""
"""
year = int(input("Enter a year: "))
if (year%4 == 0 and year%100  != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")    
    """
'''
def greet(name):
    return "HElo "+name
print(greet("vaibhav"))
'''
'''
class student:
    def __init__(self, name , age, grade):
                  self.grade =grade
                  self.name = name
                  self.age= age

    def display_details(self):
            print(f"name: {self.name}, age: {self.age}, grade: {self.grade}") 

s1 = student("vaibhav", 23, "A")
s1.display_details()

'''