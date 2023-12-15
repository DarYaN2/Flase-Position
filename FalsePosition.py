import sympy as sp

def false_position(func, a, b, tol=1e-6, max_iter=100):
    x = sp.symbols('x')
    f = sp.sympify(func)
    
    iterations = []
    iteration = 1
    
    fa = f.subs(x, a)
    fb = f.subs(x, b)
    
    if fa * fb >= 0:
        return "The function has the same sign at the endpoints. False Position method cannot be applied."
    
    while iteration <= max_iter:
        c = (a * fb - b * fa) / (fb - fa)
        fc = f.subs(x, c)
        
        iterations.append((iteration, a, b, c, fa, fb, fc))
        
        if abs(fc) < tol:
            return iterations
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
        iteration += 1
    
    return "False Position method did not converge within the specified number of iterations."

# Get user input for the function, interval [a, b]
user_func = input("Enter the function in terms of 'x': ")
a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))

iterations = false_position(user_func, a, b)

# Display iterations
if isinstance(iterations, str):
    print(iterations)
else:
    print("Iterations (iteration, a, b, c, f(a), f(b), f(c)):")
    for iteration in iterations:
        print(iteration)
