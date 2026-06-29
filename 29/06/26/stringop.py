str="Shivanand Thote"

li=["a","e","i","o","u"]

str=str.lower()

count=0
for ch in str:
    if ch in li:
        count+=1;
print(count)


