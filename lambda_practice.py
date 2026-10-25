lambda x: x * 6
def add(no1, no2):
    return no1 + no2
print(add(2, 3))
y = lambda no1, no2: no1 * no2
print(y(2, 3))
b = 8
names = ["Ada", "Bash", "Sally", "Don", "Sam"]
num = [1, 2, 3, 4, 5, 6]
a = lambda l: l + 2
print(a(4))
print(list(map(lambda x: x*2, num)))
s = list(filter(lambda name: name[0] == "S", names))
print(s)
for name in names:
    if name[-1] == "a":
        print(name)  