snowballs = int(input())
largest = 0
for snowball in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    result = (weight // time) ** quality
    if result > largest:
        largest += result
        print(f"{weight} : {time} = {int(result)} ({quality})")