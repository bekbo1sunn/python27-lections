list_ = [i for i in range(1, 25)]
res = []
for i in list_:
    s = (4 * i ** 2) + (24 - i) ** 2
    res.append(s)

print(dict(enumerate(res, 1)))
print(min(res))
