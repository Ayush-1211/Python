from collections import Counter, defaultdict, OrderedDict
import datetime

li = [1,2,1,3,5,6,3,4,2,6,8,1,6]
sentence = 'Blah Blah Blah thinking about Python'
print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(lambda : 'Does not exist!!', {'a' : 1, 'b' : 2})
print(dictionary['c'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1
print(d2 == d)

print(datetime.time(5,45,2))
print(datetime.date.today())