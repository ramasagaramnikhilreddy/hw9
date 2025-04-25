# computeFunction.py
# This program computes the function f(x) = x^2 + 2 for x from 0 to 9
# It prints the values of x and the corresponding f(x)
# No command-line arguments are required.
# Example invocation: python3 computeFunction.py

def f(x):
    return x * x + 2

def main():
    for x in range(10):  # x from 0 to 9
        result = f(x)
        print("x =", x, ", f(x) =", result)

if __name__ == "__main__":
    main()
