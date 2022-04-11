def val_checker(val):
    def _val_checker(func):
        def f(arg):
            if not(val(arg)):
                raise ValueError(f"wrong val {arg}")
            res = func(arg)
            return res

        return f

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(-5))
