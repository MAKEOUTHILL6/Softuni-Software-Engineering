movie_project = input()
rows = int(input())
column = int(input())

seats = rows * column
ticket = 0

if movie_project == "Premiere":
    ticket = 12
elif movie_project == "Normal":
    ticket = 7.50
elif movie_project == "Discount":
    ticket = 5
sales = ticket * seats
print(f"{sales:.2f} leva")