a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
D = (b ** 2) - (4 * a * c);
if D > 0:
    k = D ** 0.5;
    x1 = (-b + k) / 2 * a;
    x2 = (-b - k) / 2 * a;
    print ("Result: " + "x1 = " + str(x1) + ("   x2 = ") + str(x2));
if D == 0:
    k = D ** 0.5;
    x = (-b) / 2 * a;
    print ("Result: x = " + str(x));
if D < 0:
    k = (-D) ** 0.5;
    f = -b / 2 * a;
    s = k / 2 * a * 1j;
    x1 = f + s;
    x2 = f - s;
    print ("Result: " + "x1 = " + str(x1) + ("   x2 = ") + str(x2));