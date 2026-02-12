
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
Largest: 4
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
Leap Year
ch = input("Enter a character: ").lower()

if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant")
Consonant
num = int(input("Enter number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")
Not divisible by both 5 and 11
n = int(input("Enter N: "))
i = 1
sum = 0

while i <= n:
    sum += i
    i += 1

print("Sum:", sum)
Sum: 15
num = int(input("Enter number: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
rows = 4

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
   *
  ***
 *****
*******
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
1
12
123
1234
12345