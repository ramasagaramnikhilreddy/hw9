# cube.py
# This program prints the cube of odd numbers from 0 to 19, or the number itself if it's even.
# It uses a function cb(x) to compute the cube.
# No command-line arguments are required.
# Example invocation: python3 cube.py

def cb(x):
    return x * x * x

def main():
    for i in range(20):  # 0 to 19
        if i % 2 == 0:
            print(i)
        else:
            print(cb(i))

if __name__ == "__main__":
    main()
