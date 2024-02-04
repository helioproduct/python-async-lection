def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


def subgen():
    x = "Ready to accept message"
    message = yield x
    print("Subgen recieved", message)


@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopAsyncIteration:
            print("Done")
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

    return average
