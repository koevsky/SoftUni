name = input()
adult_tickets_count, infant_ticket_count = int(input()), int(input())
adult_tickets_price, service_cost = float(input()), float(input())
infant_ticket_price = adult_tickets_price - (adult_tickets_price * 70/100)
price = (adult_tickets_price+service_cost) * adult_tickets_count + (infant_ticket_price+service_cost) * infant_ticket_count
price *= 20/100
print(f"The profit of your agency from {name} tickets is {price:.2f} lv.")