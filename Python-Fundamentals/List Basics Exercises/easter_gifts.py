gifts_to_buy = input().split()
command = ''
while command != "No Money":
    command = input()
    info = command.split()
    action = info[0]
    product = info[1]

    if action == "OutOfStock":
        for i in gifts_to_buy:
            if product == i:
                index_n = gifts_to_buy.index(product)
                gifts_to_buy[index_n] = "None"

    elif action == "Required":
        product = info[1]
        index = int(info[2])
        if 0 < index < len(gifts_to_buy):
            gifts_to_buy[index] = product

    elif action == "JustInCase":
        gifts_to_buy[-1] = product

finished_list = []
for item in gifts_to_buy:
    if item != 'None':
        finished_list.append(item)
print(" ".join(finished_list))
