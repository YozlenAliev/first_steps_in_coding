
length_centimeters = float(input())
wide_centimeters = float(input())
high_centimeters = float(input())
filled_percentage = float(input())

volume = length_centimeters * wide_centimeters * high_centimeters
volume_in_decimeter = volume / 1000
total_water_needed = volume_in_decimeter - (volume_in_decimeter * filled_percentage) / 100

print(total_water_needed)
