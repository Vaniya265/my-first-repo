print("welcome to grade calculator")
n=int(input("enter number of subjects"))
marks=[]
for i in range(n):
    m=float(input("enter the marks of the subject"))
    marks.append(m)
    total=sum(marks)
    average=total/n
    if average>=90:
        grade="A+"
    elif average>=75:
        grade="A"
    elif average>=60:
        grade="B"
    elif average>=50:
        grade="C"
    else:
        grade="F"
print("RESULT:")
print("total marks:", total)
print("average marks:", average)
print("grade:",grade)
