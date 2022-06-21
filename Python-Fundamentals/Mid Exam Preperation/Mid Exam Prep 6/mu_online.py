base_health = 100
base_bitcoins = 0
best_room = 0
health = base_health
game_beaten = True
rooms = input().split("|")

for i in range(len(rooms)):
    room_info = rooms[i].split()
    action = room_info[0]
    best_room += 1

    if action == "potion":
        gained_hp = int(room_info[1])
        if gained_hp + health > base_health:
            gained_hp = base_health - health
            health = base_health
        else:
            health += gained_hp
        print(f"You healed for {gained_hp} hp.")
        print(f"Current health: {health} hp.")

    elif action == "chest":
        bitcoin_found = int(room_info[1])
        base_bitcoins += bitcoin_found
        print(f"You found {bitcoin_found} bitcoins.")

    else:
        attack_power = int(room_info[1])
        health -= attack_power
        if health <= 0:
            game_beaten = False
            print(f"You died! Killed by {action}.")
            print(f"Best room: {best_room}")
            break
        else:
            print(f"You slayed {action}.")

if game_beaten:
    print("You've made it!")
    print(f"Bitcoins: {base_bitcoins}")
    print(f"Health: {health}")