x = float(input())  # house high
y = float(input())  # house length
h = float(input())  # roof triangle high

front_wall = (x * x) - 1.2 * 2
back_wall = x * x
front_back_wall = front_wall + back_wall
side_wall = ((x * y) - (1.5 * 1.5)) * 2
total_green_paint = (front_back_wall + side_wall) / 3.4
side_roof = (x * y) * 2
triangle_roof = ((x * h) / 2) * 2
total_red_paint = (side_roof + triangle_roof) / 4.3

print("%.2f" % total_green_paint)
print("%.2f" % total_red_paint)
