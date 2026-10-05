def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

years = [1900, 2000, 2020, 2023, 2024]
for year in years:
    result = is_leap_year(year)
    print(f"{year}: {result}")
