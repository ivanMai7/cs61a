def square(x):
    return x*x
    
def successor(x):
    return x+1

def compose1(f,g):
"""
Return the compose function
"""
    def h(x):
        return f(g(x))
    return h

def compose2(f,g,x):
"""
Return the compose value
"""
    def h():
        return f(g(x))
    return h()

square_successor = compose1(square,successor)
print(square_successor(12))
print(compose2(square,successor,12))