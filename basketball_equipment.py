annual_tax = int(input())

trainers = annual_tax - (annual_tax * 40) / 100
equip = trainers - (trainers * 20) / 100
ball = equip * 0.25
accessories = ball * 0.20
final_price = annual_tax + trainers + equip + ball + accessories

print("%.2f" % final_price)
