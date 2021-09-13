import re

string = 'Search this inside of this text please!'
a = re.search('this',string)

print(a.span())
print(a.start())
print(a.end())
print(a.group())