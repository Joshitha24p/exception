try:
    num=int(input("Please input a number: "))
    print (num)
except ValueError as ex:
    print (ex)

try:
    num2=float(input("Please input a number: "))
    print (num2)
except ValueError as ex:
    print (ex)