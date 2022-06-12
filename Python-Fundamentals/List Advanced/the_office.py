happiness = input().split()
factor = int(input())

happiness_multi = list(map(lambda x: int(x) * factor, happiness))
filtered = list(filter(lambda x: x >= sum(happiness_multi) / len(happiness_multi), happiness_multi))

if len(filtered) >= len(happiness_multi) / 2:
    print(f"Score: {len(filtered)}/{len(happiness_multi)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(happiness_multi)}. Employees are not happy!")