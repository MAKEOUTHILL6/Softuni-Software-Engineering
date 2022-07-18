country = input().split(", ")
city = input().split(", ")

res = zip(country, city)
for key, value in res:
    print(f"{key} -> {value}")
# ------------------------------
country = input().split(", ")
city = input().split(", ")

result = {country[index]: city[index] for index in range(len(country))}
for k, v in result.items():
    print(f"{k} -> {v}")