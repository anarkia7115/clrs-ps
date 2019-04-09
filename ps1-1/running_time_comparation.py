import math


def time_to_ms(time_str):
    if time_str == 'sec':
        return 1000
    elif time_str == 'min':
        return time_to_ms('sec') * 60
    elif time_str == 'hour':
        return time_to_ms('min') * 60
    elif time_str == 'day':
        return time_to_ms('hour') * 24
    elif time_str == 'month':
        return time_to_ms('day') * 30
    elif time_str == 'year':
        return time_to_ms('day') * 365
    elif time_str == 'century':
        return time_to_ms('year') * 100
    else:
        raise Exception("UNKNWON time format!")


def fn_explain():


def find_largest_n(fn, time_str):
    MAX = 10**8
    for n in range(1, MAX):
        t_n = time_to_ms(time_str) / fn(n)
        if t_n < 1:
            return n-1
    print("n already exceed {}".format(MAX))
    return -1


def main():
    time_strs = ['sec', 'min', 'hour', 'day', 
        'month', 'year', 'century']
    fns = [
        math.log, math.sqrt, 
        lambda n: n, lambda n: n * math.log(n), 
        lambda n: n ** 2, lambda n: n ** 3, 
        lambda n: 2 ** n, lambda n: math.factorial(n)
    ]
