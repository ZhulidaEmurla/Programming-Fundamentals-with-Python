def process_todo_notes():
    todo_notes = []
    while True:
        note = input()

        if note == 'End':
            break
        todo_notes.append(note)

    sorted_notes = sorted(todo_notes, key=lambda x: int(x.split('-')[0]))
    return [note.split('-')[1] for note in sorted_notes]

result = process_todo_notes()
print(result)
