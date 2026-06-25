"""
==========================
CONTROL STATEMENTS
==========================

Loops:
1. for loop
2. while loop

=========================================
Syntax of for loop using range()
=========================================

for variable in range(limit):
    # statements

Example:
for i in range(5):
    print(i)

=========================================
Syntax of for loop using a sequence
=========================================

for variable in sequence:
    # statements

Example:
name = "Python"

for ch in name:
    print(ch)

=========================================
Syntax of for-else loop
=========================================

for variable in sequence:
    # statements
else:
    # statements

Example:
for i in range(5):
    print(i)
else:
    print("Loop completed successfully.")

=========================================
Syntax of for-else using range()
=========================================

for variable in range(limit):
    # statements
else:
    # statements

=========================================
Syntax of while loop
=========================================

while condition:
    # statements

Example:
i = 1
while i <= 5:
    print(i)
    i += 1

=========================================
Syntax of while-else loop
=========================================

while condition:
    # statements
else:
    # statements

Example:
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop completed successfully.")
"""


"""
n=int(input("Enter the number or range: "))

for i in range(0,n,2): #(start,Stop,Step)
    print(i)
"""


"""
CSE=["Shiva","Ankit","Sonu","Aditya","Ram"]

for i in CSE:
    print(i)

"""


"""
CSE=["Shiva","Ankit","Sonu","Aditya","Ram"]

for i in range(len(CSE)):

    print(f"{i+1}the Student name is: {CSE[i]}")

output: 
1the Student name is: Shiva
2the Student name is: Ankit
3the Student name is: Sonu
4the Student name is: Aditya
5the Student name is: Ram

"""

#get number form user to prints its multiplaction upto range 

# n=int(input("Enter number: "))

# for i in range(0,n):
#     i=i*5
# print(i)

"""
Chhota Bheem's father is uneducated and runs a business. Whenever he earns money, he hands it over to Chhota Bheem's mother.
Unfortunately, his mother is also uneducated. somehow she count and noted ini book After many years, Chhota Bheem joined college. One day, his father asked him to 
count all the money they had earned.Chhota Bheem decided to write a simple Python program to calculate the total amount. However, he is very weak in Python.
Help Chhota Bheem by writing a Python program to count the total money.
"""

"""
num=int(input("Enter total entryes: "))

total=0

for i in range(num):
    amount= int(input("Enter amount: "))
    total+=amount
print("Total amount is :", total)

output: 
Enter total entryes: 4 
Enter amount: 2
Enter amount: 6
Enter amount: 4
Enter amount: 7
Total amount is : 19

"""


#909write an progran is palindrome or not 

num = (input("Enter number: "))

if num == num[::-1]:
    print("palindrome")
else:
    print("not palindrome")

