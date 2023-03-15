# -------------------------------------- Task 1 -----------------------------------
def add(x, y):
    return x + y

# TODO: Add definitions of sub(), div(), mult(), exp(), as well as neg() and sqrt().
#       neg() should return the negation of the given number, and sqrt() should
#       return the square root of the given number. 

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

def exp(x, y):
    return x ** y

def neg(x):
    return x * (-1) 

def sqrt(x):
    return x ** 0.5 

# -------------------------------------- Task 2 -----------------------------------

# TODO: Implement the quadratic formula using *only* the functions defined here.
#       Do not use arithmetic operators directly. 
#       You're allowed to define other functions.

print("Let's find the roots of a quadratic function 'ax^2 + bx + c'") # instructions
print()

a = float(input("What is the value of a? a = ")) # input values
b = float(input("What is the value of b? b = "))
c = float(input("What is the value of c? c = "))

x1 = div(add(neg(b), sqrt(sub(exp(b, 2), mult(4, mult(a, c))))) , mult(2,a)) # first root of the quadratic equation
x2 = div(sub(neg(b), sqrt(sub(exp(b, 2), mult(4, mult(a, c))))) , mult(2,a)) # second root of the quadratic equation

print()
print("First root: " + str(x1)) # show results
print("Second root: " + str(x2))
