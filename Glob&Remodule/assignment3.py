import re

# Sample input list
phone_numbers = [
    "(123) 456-7090",
    "123-456-7090",
    "(999) 123-4567",
    "(123)456-7890",
    "(321) 654-0987"
]

# Regex pattern for (123) 456-7090 format
pattern = r'^\(\d{3}\) \d{3}-\d{4}$'

print("Valid Phone Numbers:")
for number in phone_numbers:
    if re.match(pattern, number):
        print(number)
