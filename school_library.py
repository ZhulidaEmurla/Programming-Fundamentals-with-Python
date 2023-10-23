shelf = input().split('&')
commands = []
while True:
    command = input()
    if command == "Done":
        break
    commands.append(command)

for command in commands:
    tokens = command.split(" | ")

    if tokens[0] == "Add Book":
        book_name = tokens[1]
        if book_name not in shelf:
            shelf.insert(0, book_name)

    elif tokens[0] == "Take Book":
        book_name = tokens[1]
        if book_name in shelf:
            shelf.remove(book_name)

    elif tokens[0] == "Swap Books":
        book1, book2 = tokens[1], tokens[2]
        if book1 in shelf and book2 in shelf:
            index1 = shelf.index(book1)
            index2 = shelf.index(book2)
            shelf[index1], shelf[index2] = shelf[index2], shelf[index1]

    elif tokens[0] == "Insert Book":
        book_name = tokens[1]
        if book_name not in shelf:
            shelf.append(book_name)

    elif tokens[0] == "Check Book":
        index = int(tokens[1])
        if 0 <= index < len(shelf):
            print(shelf[index])
print(", ".join(shelf))
