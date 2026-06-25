# no=int(input("Enter the number: "))
# match no:
#     case int()if no>0:
#         print("positive")
#     case int()if no<0:
#         print("negative")
#     case int()if no==0:
#         print("zero")


no=int(input("Enter the number: "))
match no:
    case int() if no>=0 and no<50:
        print("fail")
    case int()if no>=60 and no<50:
        print("just pass")
    case int() if no>=60 and no<70:
        print("B")
    case int()if no>=70 and no<80:
        print("B+")
    case int() if no>=80 and no<90:
        print("A")
    case int()if no>=90 and no<100:
        print("A+")
    case _:print("invalid marks")
    