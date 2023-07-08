def trace(fn):
    def traced(x):
        print('Calling ',fn,' on argument ',x)
        return fn(x)
    return traced

@trace
def squre(x):
    return x * x

@trace
def sum_squres_up_to(n):
    sum,i = 0,1
    while i <= n:
        sum,i = sum + squre(i),i + 1
    return sum
print(sum_squres_up_to(5))
