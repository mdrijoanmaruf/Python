def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

numbers = [121, 123, 1331, 10, 55, 12321]
for num in numbers:
    result = is_palindrome(num)
    print(f"{num}: {result}")
