try:
    num1, num2= eval(input("Please input two values seperated by a comma: "))
    answer=num1/num2
    print (answer)

except ZeroDivisionError:
    print ("One of the numbers are Zero, you cannot divide by 0")

except SyntaxError:
    print ("Comma is missing. Please write it like this example: 1,2")

except:
    print ("Invalid input")

else:
    print ("There are no exceptions")

finally:
    print ("This will execute no matter what.")