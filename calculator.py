num1=int(input("enter first number"))
num2=int(input("enter second number"))
print("choose operation + - * / %")
op=input("enter operation to perform")
if op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(num1/num2)
elif op=='%':
    print(num1%num2)
# else:
#     print("invalid operation choosen")