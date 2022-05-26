agency_name = input()
count_tickets_elder = int(input())
count_tickets_kids = int(input())
net_price_tickets_elder = float(input())
price_tax = float(input())

net_price_tickets_kid = net_price_tickets_elder - (net_price_tickets_elder * 0.7)
full_price_ticket_kid = net_price_tickets_kid + price_tax
full_price_ticket_elder = net_price_tickets_elder + price_tax
sum_tickets = (full_price_ticket_elder * count_tickets_elder) + (full_price_ticket_kid * count_tickets_kids)
agency_profit = sum_tickets * 0.2
print(f'The profit of your agency from {agency_name} tickets is {agency_profit:.2f} lv.')
