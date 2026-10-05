l = [22, 33, 44]

def gen():
    i = 0
    while i < 3:
        i += 1
        yield i
 #
 # res = gen()
 # print(res)
 # print('1', next(res))
 # print(2, next(res))
 # print('3', next(res))
 # for i in res:
 #     print(i)

res = (i for i in gen())
for i in res:
    print(i)


def power(n):
    return n * n
res = map(power, l)
print(list(res))

