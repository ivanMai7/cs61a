def summation(n,term):
    total,k = 0,1
    while k <= n:
        total = total + term(k)
        k = k + 1
    return total

def cube(k):
    return k * k * k

def sum_cubes(n):
    return summation(n,cube)

print(sum_cubes(3))
