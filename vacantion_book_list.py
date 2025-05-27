total_pages = int(input())
pages_readed_for_hour = int(input())
total_days_needed = int(input())

total_time_for_book = total_pages / pages_readed_for_hour
total_days = total_time_for_book / total_days_needed

print(int(total_days))
