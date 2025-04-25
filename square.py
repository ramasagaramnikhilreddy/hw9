# square.py
# This program prints the square of all numbers from 0 to 19.
# It uses a function sq(x) to compute the square.
# No command-line arguments are required.
# Example invocation: python3 square.py

def sq(x):
    return x * x

def main():
    for i in range(20):  # 0 to 19
        print("Number:", i, "Square:", sq(i))

if __name__ == "__main__":
    main()
