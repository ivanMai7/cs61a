def improve(update,close,guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def average(x,y):
    return (x + y) / 2
    
def approx_eq(x,y,tolerence=1e-15):
    return abs(x-y) < tolerence

def sqrt(a):
    def sqrt_update(x):
        return average(x,a/x)
    def sqrt_close(x):
        return approx_eq(x*x,a)
    return improve(sqrt_update,sqrt_close)

print(sqrt(4))