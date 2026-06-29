'''str="Shivanand Thote"

li=["a","e","i","o","u"]

str=str.lower()

count=0
for ch in str:
    if ch in li:
        count+=1;
print(count)


'''

'''
str1="Shivanand 852djshf"

alphacount=0
numcount=0
symbcount=0

for c in str1:
    if c.isalpha():alphacount+=1
    elif c.isdigit():numcount+=1
    elif c.isspace():pass

print(alphacount)
print(numcount)
'''


'''
#using sort function
str1="school"
str2="hoolcs"

if(sorted(str1))==(sorted(str2)):
    print("anagram")
else:
    print("not anagram")
'''


str=input("Enter string:")
count=1

for ch in str:
    if ch is " ":
        count+=1
print(count)

