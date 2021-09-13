import re

pattern = re.compile(r"([A-Za-z0-9$%#@]{7,}[0-9])")
password = 'Ayush#007'

check = pattern.search(password)

print(check)