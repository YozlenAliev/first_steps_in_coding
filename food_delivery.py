CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DELIVERY_PRICE = 2.50

chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

menu_price = (
        chicken_menu * CHICKEN_MENU_PRICE
        + fish_menu * FISH_MENU_PRICE
        + vegetarian_menu * VEGETARIAN_MENU_PRICE
)
desert_price = menu_price * 1.2
total_price = desert_price + DELIVERY_PRICE

print("%.2f" % total_price)
