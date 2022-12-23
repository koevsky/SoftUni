skumria_price = float(input())
caca_price = float(input())

palamud_weight = float(input())
safrid_weight = float(input())
midi_weight = float(input())

palamud_price = (skumria_price + (skumria_price*60/100)) * palamud_weight
safrid_price = (caca_price + (caca_price*80/100)) * safrid_weight
midi_price = midi_weight * 7.50

total_price = palamud_price + safrid_price + midi_price
print(f"{total_price:.2f}")