#Sunidhi
#Learn IT project
#Making a simple calculator

print("Press the indicated numbers for corresponding operations:\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n")

operation = int(input())
if operation == 1 or operation == 2 or operation == 3 or operation == 4:
    print("Enter two numbers: ")
    integer1 = int(input())
    integer2 = int(input())

    if operation == 1:
        print(integer1+integer2)
    elif operation == 2:
        print(integer1-integer2)
    elif operation == 3:
        print(integer1*integer2)
    elif operation == 4:
        print(integer1/integer2)
    else:
        print("Enter a valid choice")
else:
    print("Enter valid choice")
