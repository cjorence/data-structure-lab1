firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

if firstNumber < secondNumber:
    print(f"{firstNumber} is less than {secondNumber}")
elif firstNumber > secondNumber:
    print(f"{firstNumber} is greater than {secondNumber}")
elif firstNumber == secondNumber :
    print(f"{firstNumber} is equal to {secondNumber}")