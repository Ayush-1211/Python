# Scope - what variables do I have access to?
'''
    Rules:
        1. Start with local
        2. Parent local?
        3. Global
        4. Built in python function
'''
print('Example 1:')
a = 1                   # Global
def parent():           # Parent scop
    a = 10              # Parent local
    def confussion():
        return a
    return confussion()
print(parent())
print(a)

print('Example 2:')
a = 1
def parent():
    def confussion():
        return a
    return confussion()
print(parent())
print(a)

print('Example 3:')
a = 1
def parent():
    def confussion():
        return sum          # Built in Python Function
    return confussion()
print(parent())
print(a)