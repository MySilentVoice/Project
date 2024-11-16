# python program to print hello world
print('Hello, World')

# python program to input 2 numbers and perform basic operations
a = int(input('enter a: '))
b = int(input('enter b: '))
print(f'a + b {a + b}')
print(f'a - b {a - b}')
print(f'a * b {a * b}')
print(f'a / b {a / b}')
print(f'a ^ b {a**b}')

# python program to print number is even or odd
c = int(input('enter c: '))
if c % 2 == 0:
    print('even')
else: 
    print('odd')

# py program num is divisible by 3 or not . if divisible by three also check if it is divisible by five
d = int(input('enter d: '))
if d % 3 == 0:
    print('divisible by 3')
    if d % 5 == 0:
        print('divisible by 5')
    else: 
        print('not divisible by 5')
else: 
    print('divisible by 3')


# basic atm program allow user ot check balance, deposit money and withdraw money

# python program to print all even from 1 to 100
for i in range(1,100):
    if i % 2 == 0:
        print(i, end = ', ')

# python program to print table of any number given by user
e = int(input('enter e: '))
for i in range(1, 11): 
    print(f'{e} X {i} = {e*i}')

# python program to print fibonaci series
def fib(f):
    if f == 0:
        return 0
    elif f == 1:
        return 1
    else:
        return fib(f-1) + fib(f-2)

f = int(input('Enter a number: '))
print(fib(f))

# py program to input a number to check if it's palendrome or not
def is_palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        digit = n % 10 
        rev = rev * 10 + digit
        n //= 10
    return temp == rev
g = int(input('enter g: '))
print(is_palindrome(g))

# py program to input length of list and create a list dynamically hence search form the list using linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

h = int(input('enter hL: '))
list1 = []
for i in range(h):
    item = input('enter element to add: ')
    list1.append(item)

x = input('enter element to search: ') 
res = linear_search(list1, x)

if res != -1:
    print(f'Element found at index: {res}')
else:
    print('Element not found.')

# py program to create a dictionary containing student data (name, roll number, course id) giving input roll number and print course id
def new_student():
    student_data = {}
    n = int(input('enter number of students: '))
    for i in range(n):
        name = input("Enter the student's name: ")
        roll_num = input("Enter the roll number: ")
        course_id = input("Enter the course ID: ")
        student_data[roll_num] = (name, course_id)
    return student_data

def get_course_id(student_data, roll_num):
    if roll_num in student_data:
        return student_data[roll_num][1] 
    else:
        return None

student_data = new_student()

roll_number = input("Enter the roll number to find the course ID: ")
course_id = get_course_id(student_data, roll_number)

if course_id:
    print(f"The course ID for roll number {roll_number} is: {course_id}")
else:
    print(f"No records found for roll number {roll_number}.")

# python program of square made of * and right triangle made of *
n = int(input('enter rows: '))
for i in range(n):
    for j in range(n):
        print('*', end = ' ')
    print()

for i in range(n):
    for j in range(0, i + 1):
        print('*', end = '')
    print()
# py program to swap two numbers using third variable second, without using single variable and in a single line
x = int(input('enter x: '))
y = int(input('enter y: '))
temp = x
x = y
y = temp
print(f'{x}, {y}')
x,y = y,x
print(f'{x}, {y}')

# python function to check even or odd
x = int(input('enter c: '))
def odd_even(x):
    if c % 2 == 0:
        return 'even'
    else: 
        return 'odd'

# py function to print factorial without recursion
def fact(n):
    facto = 1
    for i in range(1, n + 1):
        facto = facto * i
    return facto

# py function accepts any number of parameter and returns sum, product, avg
def calc(*args):
    sum = 0
    product = 1
    avg = 0
    for num in args:
        sum += num
    for num in args:
        product *= num
    for num in args:
        avg = sum/len(args)
    return {'sum': sum, 'product': product, 'average': avg}

# py finction to return sum?

# py function takes list and return rnadomised list
import random
def suff(list1):
    n = len(list1)
    for i in range(n):
        j = random.randint(0, n - 1)
        list1[i], list1[j] = list1[j], list1[i]
    return list1
print(suff([1, 2, 3, 4, 5, 6, 7]))