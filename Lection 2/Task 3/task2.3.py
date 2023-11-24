max_number = int(input("Enter a max number: "))
divider_nmbrs = []
prime_nmbrs = []
current_number = 0
while current_number < max_number: 
    current_number += 1
    divider = 1   
    while divider <= current_number:
        if (current_number % divider) == 0:
            divider_nmbrs.append(divider)
        divider += 1
    string = "{current}\t | {dividers}\n".format(current = current_number, dividers = divider_nmbrs)
    print(string)
    if len(divider_nmbrs) == 2:
        prime_nmbrs.append(divider_nmbrs[-1])
    divider_nmbrs.clear()
print(prime_nmbrs)