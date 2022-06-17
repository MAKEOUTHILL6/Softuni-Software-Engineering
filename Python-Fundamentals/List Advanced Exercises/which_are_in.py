wanted_seq = input().split(", ")

seq = input().split(", ")
new_seq = [e for e in wanted_seq if e in '\n'.join(seq)]
print(new_seq)

