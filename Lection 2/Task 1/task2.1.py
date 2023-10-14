user_list = [];
quanity = int(input("How many elements do you wanna add?: "));
while quanity > 0:
    element = input("Your element: ")
    user_list.append(element)
    quanity -= 1;
list_set = set(user_list);
unique_list = list(list_set)
print(unique_list)