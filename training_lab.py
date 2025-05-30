w = float(input())
h = float(input())

workbench_h = 0.70
workbench_w = 1.20
coridor_h = 1.00
total_h = (h - coridor_h) // workbench_h
total_w = w // workbench_w
total_workbenches = (total_h * total_w) - 3

print(int(total_workbenches))