grocery_list = input().split("!")


def add_item(item):
    if item not in grocery_list:
        grocery_list.insert(0, item)


def remove_item(item):
    if item in grocery_list:
        grocery_list.remove(item)


def correct_item(old_item, new_item):
    if old_item in grocery_list:
        index = grocery_list.index(old_item)
        grocery_list[index] = new_item


def rearrange_item(item):
    if item in grocery_list:
        grocery_list.remove(item)
        grocery_list.append(item)


while True:
    command = input()
    if command == "Go Shopping!":
        break

    command_parts = command.split()
    action = command_parts[0]

    if action == "Urgent":
        add_item(command_parts[1])
    elif action == "Unnecessary":
        remove_item(command_parts[1])
    elif action == "Correct":
        correct_item(command_parts[1], command_parts[2])
    elif action == "Rearrange":
        rearrange_item(command_parts[1])

print(", ".join(grocery_list))
