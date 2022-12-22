# def f(x):
#     x ** 2
#
# g = f
# print(type(f))
# print(f(1))
# print(g(1))

# def f(x):
#     return x**2
#
# g = f
# print(type(f))
# print(f(2))
# print(g(4))


# def calc1(x):
#     return x+10
#
# print(calc1(10))
#
# def calc2(x):
#     return x*10
#
# print(calc2(10))
#
# def math(op,x):
#     print(op(x))
#
# math(calc2,10)
# # math(calc1,10)
#
# def sum(x, y):
#     return x + y


sum = lambda x, y: x + y


# def mylt(x, y):
#     return x * y
#
#
# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a,b)
#
#
# calc(f, 5, 10)


def calc (op,a,b):
    print(op(a,b))

print(sum(5, 10))
calc(lambda x, y: x+y, 4,5)
