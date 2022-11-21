a = 5
print(a)
print(type(a))

a = "jedynka"
print(a)
print(type(a))

g: float
g = 5.776
print(g)
print(type(g))

g = True
print(g)
print(type(g))

n = 9

def policz(a: int, b: int, c: int, y: int) -> int:
    global n
    n = (a + b) * y - c + n
    return n


print(policz(3, 4, 7, 11))
print(policz(3, 4.4, 7, 9.93))
print(policz(True, 4.4, 7, 9.93))

print(n)

print((lambda r:r*4)(3))

num = [5,3,2,11,-32,0,13,122,6,9,10]
