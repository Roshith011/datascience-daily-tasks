
#  Write a function that takes the radius of a circle and returns its area.

def circle_area(radius):
    pi = 3.1416   # manually defined value of pi
    return pi * radius * radius

print(circle_area(5))
78.54
# Write a function that accepts three numbers and returns the largest one.

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example
print(largest(10, 25, 15))
25
# Write a function that takes a string and returns its length without using built-in length functions.

def string_length(text):
    count = 0
    for char in text:
        count += 1
    return count

# Example
print(string_length("Hello"))
5
# Write a function that checks whether a number is prime.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Example
print(is_prime(7))
True
# Write a recursive function to find the nth Fibonacci number.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Example
print(fibonacci(6))
8
# Write a recursive function to reverse a string.

def reverse_string(text):
    if len(text) == 0:
        return text
    return text[-1] + reverse_string(text[:-1])

# Example
print(reverse_string("Hello"))
olleH
#  Write a program to find the sum of all numbers from 1 to n using a for loop.

def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_n(10))
55
# Write a program to count how many even numbers are present in a list.

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

print(count_even([10, 15, 22, 33, 40, 55]))
3
# Write a program to print all prime numbers between 1 and 100.

def print_primes():
    for num in range(1, 101):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)

print_primes()
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
