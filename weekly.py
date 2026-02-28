print("-------------- Que 1(A) --------------")
# Find the output
a = [1,2,3]
b = a
c = a[:]                             # [2, 4, 6,8][2, 4, 6, 8][1, 2, 3, 5]
b.append(4)
c.append(5)
for i in range (len(a)):
    a[i] = a[i] * 2
    print(a, b, c)


print("-------------- Que 1(B) --------------")
# Predict the output:
x = [1, [2, 3], 4]
y = x[:]

x[1].append(5)
y[0] = 10

print(x, y)


print("-------------- Que 1(C) --------------")
# Find the output:
s = "PYTHON"
res = ""

for i in range(len(s)):
    if i % 2 == 0:
        res += s[i].lower()
    else:
        res += s[i]

print(res)


print("-------------- Que 1(D) --------------")
# Predict the output:
x = [i for i in range(10) if i % 2 != 0 and i < 7]
print(x)


print("-------------- Que 1(E) --------------")
# Find the output:
def func(x, lst=[]):
    lst.append(x)
    return lst

print(func(1))
print(func(2, []))
print(func(3))


print("-------------- Que 1(F) --------------")
# Find the output:
def test(a):
    a = a + [4]
    return a

x = [1,2,3]
y = test(x)
print(x, y)


print("-------------- Que 1(G) --------------")
# Find the output:
a = [1,2,3,4]
for i in range(len(a)):
    a[i] = a[i] * i
print(a)


print("-------------- Que 1(H) --------------")
# Find the output:
def f(x):
    return x + 2

def g(x):
    return f(x) * 2

print(g(3))


