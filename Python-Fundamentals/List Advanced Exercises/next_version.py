version = input().split(".")
version_new = int("".join(version)) + 1
result = [str(el) for el in str(version_new)]
print(".".join(result))