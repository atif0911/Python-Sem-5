try:
    n1,n2=map(float,input("Enter two numbers: ").split(','))
    result = n1 / n2
    print(f"The result of {n1} divided by {n2} is {result}.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed. Please enter a non-zero denominator.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values seperated by comma.")
except SyntaxError:
    print("Error: There was a syntax error in your input. Please check the format.")