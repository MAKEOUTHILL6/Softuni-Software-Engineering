def wolf(animals):
    for animal in range(len(animals)):
        if animals[animal] == "wolf":
            if animals[-1] == "wolf":
                print("Please go away and stop eating my sheep")
            else:
                animal_position = len(animals) - animals.index("wolf") - 1
                print(f"Oi! Sheep number {animal_position}! You are about to be eaten by a wolf!")


animals = input().split(", ")
wolf(animals)