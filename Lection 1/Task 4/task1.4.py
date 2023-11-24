SymbolX = int(input("Select a number of symbol: 1, 2, 3, 4, 5, 6:  "));
number1 = int(input("Enter first number: "));
number2 = int(input("Enter second number: "));
match SymbolX:
    case 1:
        resulta = number1 + number2
    case 2:
        resulta = number1 - number2
    case 3: 
        resulta = number1 * number2
    case 4:
        resulta = number1 / number2
    case 5:
        resulta = number1 ** (1 / number2)
    case 6:
        resulta = number1 ** number2
print ("Result: " + str(resulta))