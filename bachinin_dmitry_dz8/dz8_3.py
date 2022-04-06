import functools as fun


def type_logger(func):

    @fun.wraps(func) # Как работает маскировка, я не совсем понял, как ее писать?
    def f(*args):
        res = func(*args)
        res_str = ""
        for num in res:
            type_res = type(num)
            res_str += f"{func.__name__} ({num}: {type_res})\n"
        return res_str
    return f

@type_logger
def calc_cube(*x):
    return (num**3 for num in x)


print(calc_cube(3,2,5))