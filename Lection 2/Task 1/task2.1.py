user_list = []
element = str
while element != 'stop':
    element = input("Enter your element, but if u wanna stop enter stop: ")
    user_list.append(element)
list_set = set(user_list)
unique_list = list(list_set)
print(unique_list)