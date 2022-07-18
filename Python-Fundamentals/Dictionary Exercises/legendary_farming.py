def get_info(sp_item, junk, legendary_items):
    print(f"{sp_item} obtained!")
    print(f"shards: {legendary_items['shards']}")
    print(f"fragments: {legendary_items['fragments']}")
    print(f"motes: {legendary_items['motes']}")
    for key, value in junk.items():
        print(f"{key}: {value}")


legendary_items = {"shards": 0, "motes": 0, "fragments": 0}
junk = {}
condition = False

while True:
    elements = input().lower()
    elements = elements.split(" ")
    for item in range(0, len(elements), 2):
        item_name = elements[item + 1]
        item_value = int(elements[item])

        if item_name in ["shards", "motes", "fragments"]:
            if item_name not in legendary_items.keys():
                legendary_items[item_name] = 0
            legendary_items[item_name] += int(item_value)

            if legendary_items[item_name] >= 250:
                legendary_items[item_name] -= 250
                special_item = ''
                if item_name == "shards":
                    special_item = "Shadowmourne"

                if item_name == "motes":
                    special_item = "Dragonwrath"

                if item_name == "fragments":
                    special_item = "Valanyr"

                get_info(special_item, junk, legendary_items)
                condition = True

        else:
            if item_name not in junk:
                junk[item_name] = 0
            junk[item_name] += int(item_value)

        if condition:
            break

    if condition:
        break
