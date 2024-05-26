def f(a):
    print(a*3)

def g(a):
    return a*3

def h(*a):
    return sum(a)

def i(**a):
    print(a.keys())


print(type(f(2)))
print(type(g(2)))
print(h(1,2,3,4,5))
print(i(hello="key",b="hello",c="gello"))


