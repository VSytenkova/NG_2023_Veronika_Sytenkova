sistema = int(input("if u wanna translation from Celsius enter 1, if from Fahrenheit enter 2"));
temperature = int(input("enter temperature"));
if sistema == 1: 
    result = (temperature * 1.8) + 32;
if sistema == 2: 
    result = (temperature - 32) / 1.8;
print (format(result))