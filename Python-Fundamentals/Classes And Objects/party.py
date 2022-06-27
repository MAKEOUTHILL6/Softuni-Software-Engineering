def adding(party, line):
    while line != "End":
        party.people.append(line)
        line = input()

    return party


class Party:
    def __init__(self):
        self.people = []


party = Party()
line = input()
adding(party, line)
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
