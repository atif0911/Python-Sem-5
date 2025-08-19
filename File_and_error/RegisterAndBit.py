def check_range(x):
    return 1 <= x <= 255

def find_n(x):
    n=0
    while 2**n<x:
        n+=1
    return n
while True:
    try:
        x = int(input("Enter Number of Registers in CPU:"))
        if not check_range(x):
            raise ValueError("Number out of range.")
        n = find_n(x)
        print(f"The number of bits for the register field in the instruction format is {n}.")
        break
    except ValueError as e:
        print(f"Error: {e}. Please try again.")
    except SyntaxError:
        print("Error: There was a syntax error in your input. Please check the format.")