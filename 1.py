# 1. Variables and Data Types
name = "Kael"                 # string
age = 22                      # integer
height = 5.9                  # float
is_cool = True                # boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Cool person:", is_cool)
print("Type of 'age':", type(age))  # check type

print("\n---\n")

# 2. Input and Output
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

print("\n---\n")

# 3. Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

print("\n---\n")

# 4. Comparison and Logical Operators
x = 7
y = 5
print("x > y:", x > y)
print("x == y:", x == y)
print("x != y:", x != y)
print("Logical AND:", x > 5 and y < 10)
print("Logical OR:", x < 5 or y < 10)
print("Logical NOT:", not(x < 5))

print("\n---\n")

# 5. If-Else Statements
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

print("\n---\n")

# 6. Loops (for and while)
print("For loop from 1 to 5:")
for i in range(1, 6):
    print(i)

print("While loop from 5 to 1:")
count = 5
while count > 0:
    print(count)
    count -= 1

print("\n---\n")

# 7. Lists and List Operations
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print("Fruits list:", fruits)
print("First fruit:", fruits[0])
fruits.remove("banana")
print("Updated fruits list:", fruits)

print("\n---\n")

# 8. Tuples
coordinates = (10, 20)
print("Tuple:", coordinates)
print("X-coordinate:", coordinates[0])

print("\n---\n")

# 9. Dictionaries
person = {"name": "Kael", "age": 22, "country": "India"}
print("Name:", person["name"])
person["age"] = 23  # updating value
print("Updated person:", person)

print("\n---\n")

# 10. Functions
def greet(name):
    print(f"Hello, {name}!")

greet("Kael")

def add(a, b):
    return a + b

print("Sum of 3 and 4:", add(3, 4))

print("\n---\n")

# 11. Exception Handling
try:
    num = int(input("Enter a number to divide 10 by: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number.")

print("\n---\n")

# 12. Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

person1 = Person("Kael", 22)
person1.say_hello()


# 13. String Methods & Manipulation

text = " Hello World! "
print(text.lower())
print(text.strip())
print(text.replace("World", "Kael"))
print("Kael" in text)

# 14. List Comprehensions

for x in range(0, 6):
    print(f"{x} squared is {x**2}")

