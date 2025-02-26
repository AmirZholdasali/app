import re

#reading files
with open("row.txt", encoding="utf-8") as file:
    text = file.read()

# 1. 'a' followed by zero or more 'b's
def match_a_b():
    return re.findall(r'ab*', text)

# 2. 'a' followed by two to three 'b's
def match_a_bbb():
    return re.findall(r'ab{2,3}', text)

# 3. Sequences of lowercase letters joined with an underscore
def find_underscore_sequence():
    return re.findall(r'[a-z]+_[a-z]+', text)

# 4. One uppercase letter followed by lowercase letters
def find_upper_lower():
    return re.findall(r'[A-Z][a-z]+', text)

# 5. 'a' followed by anything, ending in 'b'
def match_a_any_b():
    return re.findall(r'a.*b', text)

# 6. Replace spaces, commas, or dots with a colon
def replace_chars():
    return re.sub(r'[ ,.]', ':', text)

# 7. Convert snake_case to CamelCase
def snake_to_camel():
    return re.sub(r'_(\w)', lambda m: m.group(1).upper(), text)

# 8. Split string at uppercase letters
def split_at_uppercase():
    return re.split(r'(?=[A-Z])', text)

# 9. Insert spaces between words starting with capital letters
def insert_spaces():
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

# 10. Convert CamelCase to snake_case
def camel_to_snake():
    return re.sub(r'([A-Z])', r'_\1', text).lower().lstrip('_')

#testing

print("1:", match_a_b())
print("2:", match_a_bbb())
print("3:", find_underscore_sequence())
print("4:", find_upper_lower())
print("5:", match_a_any_b())
print("6:", replace_chars())
print("7:", snake_to_camel())
print("8:", split_at_uppercase())
print("9:", insert_spaces())
print("10:", camel_to_snake())
