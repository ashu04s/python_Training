def square(x):
    return x * x


def calc(func, value):
    return func(value)


result = calc(square, 5)

print(result)