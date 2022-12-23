page_count = int(input())
pages_per_hour = int(input())
days_count = int(input())

pages_per_day = page_count / days_count
hours_per_day = pages_per_day // pages_per_hour
print(int(hours_per_day))