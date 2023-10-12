sistema = int(input("if u wanna translation from Celsius enter 1, if from Fahrenheit enter 2: "));
temperature = int(input("Enter temperature: "));
if sistema == 1: 
    result = (temperature * 1.8) + 32;
    print ("In Fahrenheit it's: " + (str(result)));
if sistema == 2: 
    result = (temperature - 32) / 1.8;
    print ("In Celsius it's: " + (str(result)))