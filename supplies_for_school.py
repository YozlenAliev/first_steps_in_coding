PACKAGE_PENS_PRICE = 5.80
PACKAGE_MARKERS_PRICE = 7.20
CLEANING_FLUID_PRICE = 1.2

package_pens = int(input())
package_markers = int(input())
cleaning_fluid = int(input())
discount = int(input())

total_pens = package_pens * PACKAGE_PENS_PRICE
total_markers = package_markers * PACKAGE_MARKERS_PRICE
total_cleaning_fluid = cleaning_fluid * CLEANING_FLUID_PRICE
discount_percent = discount / 100
total_price_before_discount = total_pens + total_markers + total_cleaning_fluid
total_price = total_price_before_discount - total_price_before_discount * discount_percent

print(total_price)
