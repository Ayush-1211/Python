import re

pattern = re.compile('this')
string = 'Search this inside of this text please!'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)

print(a)
print(b)
print(c)