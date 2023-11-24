user_list = []
filtered_list = []
quanity = int(input("How many elements do u wanna add?: "))
while quanity > 0:
    element = input("Your element: ")
    user_list.append(element)
    quanity -= 1

item_num = -1

for item in user_list:
     if item_num == len(user_list):
          break
     elif item.isdigit():
           filtered_list.append(item)
     item_num += 1 

print("Numbers in your list: " + len(filtered_list))