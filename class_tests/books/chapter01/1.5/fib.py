def fib(n):
    """ Calculate the nth value of the fibonacci number when n >= 2 """
    pred,curr = 0,1
    k = 2
    while k < n:
        pred,curr = curr,curr + pred
        k = k + 1
    return curr
    
result = fib(8)

print(result)

#The use of assert test
assert fib(8) == 13,'Wrong answer,fib(8) should be 13'