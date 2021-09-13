import re

pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
string = 'ayushprajapati1211@gmail.com'

a = pattern.search(string)

print(a)