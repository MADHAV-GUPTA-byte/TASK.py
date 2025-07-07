num=int(input("Enter a number: "))
if num !=0:
    if num%2==0:
        print(num, "is an even")
    elif num%2!=0:
        print(num,"is an odd")
    else :
        print("not a number")
else:
    print("the number is",num)
