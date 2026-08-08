valid=False
while not valid:
    try:
        n=int(input("Please input an even number: "))
        while n%2==0:
            print ("bye")
        valid=True
    except ValueError:
        print ("Invalid")