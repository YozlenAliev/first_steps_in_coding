vege = float(input())
fruits = float(input())
price_vege = int(input())
price_fruits = int(input())
total_vege = vege * price_vege
total_fruits = fruits * price_fruits
total = (total_vege + total_fruits) / 1.94

print("%.2f" % total)