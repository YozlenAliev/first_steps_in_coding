
# 1_E
deposit = int(input())
deposit_monts = int(input())
annual = float(input())

# 2_T
annual_percentage = annual / 100
final_price = deposit + deposit_monts * ((deposit * annual_percentage) / 12)

# 3_L
print(final_price)
