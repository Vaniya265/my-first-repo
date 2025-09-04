print("welcome to temperature converter")
print("choose the converter")
print("1. celcius to fahrenheit")
print("2. celcius to kelvin")
print("3. kelvin to celcius")
choice=int(input("select a choice from 1 to 3"))
if choice==1:
    c=float(input("enter a temperature in celcius"))
    print(c*(9/5)+32)
elif choice==2:
    c=float(input("enter a temperature in celcius"))
    print(c+273.5)
elif choice==3:
    k=float(input("enter a temperature in kelvin"))
    print(k-273.15)
else:
    print("invalid choice")



