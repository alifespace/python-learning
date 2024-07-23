def f1(a, b, c, *args, **kwargs):
    print(a, b, c)
    print(args)
    print(type(kwargs), kwargs)

f1(1, 2, 3, 4, 5, kw_a=1, kw_b=2)