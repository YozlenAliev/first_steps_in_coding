square_meter = float(input())
price: float = square_meter * 7.61
discount: float = price * 0.18
final_price: float = price - discount


print (f'The final price is: {final_price} lv.')
print (f'Discount is: {discount} lv.')