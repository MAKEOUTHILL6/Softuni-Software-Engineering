electrons = int(input())
shell = []
position = 1

while True:
    element = 2 * (position ** 2)

    if element < electrons:
        electrons -= element
        shell.append(element)
    else:
        shell.append(electrons)
        break

    position += 1
print(shell)