# cube.py
# Description:
# This script prints numbers from 0 to 19. If the number is odd, it prints its cube.
# If the number is even, it simply prints the number itself.
#
# Command line arguments:
# None
#
# Example invocation:
# python3 cube.py

# Function to return the cube of a number
def cb(x):
    return x * x * x

# Main function to loop through numbers 0–19
def main():
    for i in range(20):  # Loop from 0 to 19
        if i % 2 == 0:
            print(i)       # Even number: print as is
        else:
            print(cb(i))   # Odd number: print cube

# Entry point of the script
if __name__ == "__main__":
    main()
