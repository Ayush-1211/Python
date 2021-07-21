class A:
    num = 10
class B(A):
    pass
class C(A):
    num = 1
class D(B,C):
    pass

print(D.mro())      # It'll show the path. How it will go through and access the num
print(D.__mro__)
print(D.num)