rooms = int(input())
free_chairs = 0
is_Enough = True
for room in range(1, rooms + 1):
    chairs, visitors = input().split()

    if len(chairs) >= int(visitors):
        free_chairs += len(chairs) - int(visitors)
    else:
        is_Enough = False
        print(f"{abs(len(chairs) - int(visitors))} more chairs needed in room {room}")

if is_Enough:
    print(f"Game On, {free_chairs} free chairs left")