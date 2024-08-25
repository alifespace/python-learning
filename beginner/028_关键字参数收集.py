# 实参的顺序：位置（普通）参数、*args（收集参数）、关键字参数、**kwargs（关键字收集参数）
def f1(a, b, c, *args, **kwargs):
    print(a, b, c)
    print(args)
    print(type(kwargs), kwargs)  # 关键字参数收集，会把多余的关键字参数收集成字典

f1(1, 2, 3, 4, 5, kw_a=1, kw_b=2)