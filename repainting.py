NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
PAINT_THINNER_PRICE = 5
BAGS_PRICE = 0.4

nylon = int(input())
paint = int(input())
paint_thinner = int(input())
work_hours = int(input())

nylon_needed = (nylon + 2) * NYLON_PRICE
paint_needed = (paint * 1.1) * PAINT_PRICE
paint_thinner_needed = paint_thinner * PAINT_THINNER_PRICE
total_price_materials = nylon_needed + paint_needed + paint_thinner_needed + BAGS_PRICE
total_work_price = work_hours * 0.30 * total_price_materials
total_price = total_price_materials + total_work_price

print(total_price)
