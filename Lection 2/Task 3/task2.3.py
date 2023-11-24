max_number = int(input("Enter a max number: "))
divider_nmbrs = []
prime_nmbrs = []
qurent_number = 0
while qurent_number < max_number: 
    qurent_number += 1
    divider = 1   
    while divider <= qurent_number:
        if (qurent_number % divider) == 0:
            divider_nmbrs.append(divider)
        divider += 1
    string = "{qurent}\t | {dividers}\n".format(qurent = qurent_number, dividers = divider_nmbrs)
    print(string)
    if len(divider_nmbrs) == 2:
        prime_nmbrs.append(divider_nmbrs[-1])
    divider_nmbrs.clear()
print(prime_nmbrs)