# 08_basic_programs.py
# Beginner Python Programs

a = 10
b = 20

print("1. Addition")
print("Result:", a + b)

number = 15

print("\n2. Even or Odd")

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

x = 25
y = 40
z = 15

largest = max(x, y, z)

print("\n3. Largest Number")
print("Largest:", largest)

marks = [80, 75, 90, 85, 70]

average = sum(marks) / len(marks)

print("\n4. Average Marks")
print("Average:", average)

num1 = 20
num2 = 10

print("\n5. Simple Calculator")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
