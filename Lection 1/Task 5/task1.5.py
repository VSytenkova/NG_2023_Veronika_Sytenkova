a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
D = b ** 2 - 4 * a * c
if D > 0:
    square = D ** 0.5
    x1 = (-b + square) / 2 * a
    x2 = (-b - square) / 2 * a
    print ("Result: " + "x1 = " + str(x1) + "   x2 = " + str(x2))
if D == 0:
    x = (-b) / 2 * a
    print ("Result: x = " + str(x))
if D < 0:
    square = (-D) ** 0.5
    x1 = (-b / 2 * a) + (square / 2 * a * 1j)
    x2 = (-b / 2 * a) - (square / 2 * a * 1j)
    print ("Result: " + "x1 = " + str(x1) + "   x2 = " + str(x2))