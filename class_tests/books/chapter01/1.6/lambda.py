def compose1(f,g):
    return lambda x : f(g(x))
    
square_successor = compose1(lambda x : x*x,lambda x : x+1)
print(square_successor(12))