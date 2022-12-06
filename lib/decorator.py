from time import perf_counter
# from functools import wraps

def count_timer(func):

    def inner(*args, **kwargs):
        start = perf_counter()
        res = func(*args, **kwargs)
        finish = perf_counter()
        counter = (finish - start)
        print(f'{func.__name__} took: {counter}ms')
        return res
    return inner




