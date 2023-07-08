def summation(n,term):
    total,k = 0,1
    while k <= n:
        total = total + term(k)
        k = k + 1
    return total

def cube(k):
    return k * k * k

def identity(k):
    return k

def square(k):
    return k * k
    
def pi_term(k):
    return 8 / ((4*k - 3) * (4*k - 1))

def sum_cubes(n):
    return summation(n,cube)

def sum_naturals(n):
    return summation(n,identity)

def pi_sum(n):
    return summation(n,pi_term)

print(sum_cubes(3))
print(sum_naturals(3))
print(summation(10,square))
print(pi_sum(1e6))