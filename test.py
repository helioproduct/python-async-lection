def fun():
    for i in range(100):
        yield i


test = fun()
print(list(test))
