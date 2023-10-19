dungeon_rooms = input().split("|")
health = 100
bitcoins = 0
room_number = 0

for room in dungeon_rooms:
    room_number += 1
    command, value = room.split()
    value = int(value)

    if command == "potion":
        if health + value > 100:
            healed_amount = 100 - health
            health = 100
        else:
            healed_amount = value
            health += value
        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_number}")
            break

if health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
