def is_winning(ticket):
    if len(ticket) != 20:
        return 'invalid ticket'
    left_side = ticket[:10]
    right_side = ticket[10:]
    winning_symbols = ["@", "$", "#", "^"]
    for winning_symbol in winning_symbols:
        for repetition in range(10, 5, -1):
            winning_symbol_rep = winning_symbol * repetition
            if winning_symbol_rep in left_side and winning_symbol_rep in right_side:
                if repetition == 10:
                    return f'ticket "{ticket}" - {repetition}{winning_symbol} Jackpot!'
                return f'ticket "{ticket}" - {repetition}{winning_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = input()
data = [ticket.strip() for ticket in tickets.split(", ")]


for ticket in data:
    print(is_winning(ticket))