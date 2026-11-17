def main():
    a, b = 0, 0
    
    while True:
        a = float(input("What's a? "))
        b = float(input("What's b? "))
        
        if a != b:
            break
        print("a and b cannot be equal")
    
    fa = polynomial(a)
    fb = polynomial(b)
    
    rate_of_change = (fb - fa) / (b - a)
    print(f"For a = {a} and b = {b}:\n- f({a}) = {fa}\n- f({b}) = {fb}\n- Avg rate of change = {rate_of_change}")
    

def polynomial(x):
    return (2*(x**2) + 3*x + 1)


main()
