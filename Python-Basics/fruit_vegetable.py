product = input()

fruits = product == "banana" or product == "apple" or product == "kiwi" or product == "cherry" or product == "lemon" or\
         product == "grapes"
vegetables = product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot"

if fruits:
    print("fruit")
elif vegetables:
    print("vegetable")
else:
    print("unknown")
