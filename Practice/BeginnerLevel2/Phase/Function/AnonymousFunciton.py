
x = lambda name : name
print(x("Songporworn"))
cal= lambda A1,A2 : A1*A2
print(cal(12,15))


def Summary(a):
    return lambda x : a**x

result = Summary(2)
print(result(5))

