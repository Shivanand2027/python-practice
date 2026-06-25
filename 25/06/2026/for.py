"""
==========================
FOR LOOP IN PYTHON
==========================

Definition:
------------
A for loop is used to iterate over a sequence (list, tuple, string,
dictionary, set) or a range of numbers.

==========================
Syntax of for loop
==========================

for variable in sequence:
    # statements

Example:
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)

Output:
Apple
Banana
Orange

==========================
Syntax of for loop using range()
==========================

for variable in range(stop):
    # statements

Example:
for i in range(5):
    print(i)

Output:
0
1
2
3
4

==========================
Syntax of range(start, stop)
==========================

for variable in range(start, stop):
    # statements

Example:
for i in range(1,6):
    print(i)

Output:
1
2
3
4
5

==========================
Syntax of range(start, stop, step)
==========================

for variable in range(start, stop, step):
    # statements

Example:
for i in range(0,11,2):
    print(i)

Output:
0
2
4
6
8
10

==========================
Loop through String
==========================

name = "Python"

for ch in name:
    print(ch)

Output:
P
y
t
h
o
n

==========================
Loop through List
==========================

students = ["Shiva","Ankit","Sonu","Aditya","Ram"]

for student in students:
    print(student)

Output:
Shiva
Ankit
Sonu
Aditya
Ram

==========================
Using range(len())
==========================

students = ["Shiva","Ankit","Sonu","Aditya","Ram"]

for i in range(len(students)):
    print(f"{i+1}. {students[i]}")

Output:
1. Shiva
2. Ankit
3. Sonu
4. Aditya
5. Ram

==========================
Multiplication Table
==========================

num = int(input("Enter number: "))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

Output:
Enter number: 5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50

==========================
Sum of N Numbers
==========================

n = int(input("Enter total entries: "))

total = 0

for i in range(n):
    amount = int(input("Enter amount: "))
    total += amount

print("Total =", total)

Output:
Enter total entries: 4
Enter amount: 5
Enter amount: 8
Enter amount: 6
Enter amount: 1
Total = 20

==========================
for-else Loop
==========================

for i in range(5):
    print(i)
else:
    print("Loop completed successfully.")

Output:
0
1
2
3
4
Loop completed successfully.

==========================
break Statement
==========================

for i in range(10):
    if i == 5:
        break
    print(i)

Output:
0
1
2
3
4

==========================
continue Statement
==========================

for i in range(6):
    if i == 3:
        continue
    print(i)

Output:
0
1
2
4
5

==========================
pass Statement
==========================

for i in range(5):
    pass

print("Program Finished")

Output:
Program Finished

==========================
Nested for Loop
==========================

for i in range(3):
    for j in range(2):
        print(i, j)

Output:
0 0
0 1
1 0
1 1
2 0
2 1

==========================
Palindrome Program
==========================

num = input("Enter number: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

Output:
Enter number: 909
Palindrome

==========================
Important Points
==========================

1. A for loop is used to iterate over iterable objects.
2. range() generates a sequence of numbers.
3. break terminates the loop.
4. continue skips the current iteration.
5. pass does nothing (placeholder).
6. else executes only if the loop finishes without break.
7. Nested loops are loops inside another loop.
8. Python uses indentation instead of braces {}.

==========================
Time Complexity
==========================

Traversing List      : O(n)
Traversing String    : O(n)
Traversing Tuple     : O(n)
Traversing Dictionary: O(n)
Nested Loop          : O(n × m)

"""