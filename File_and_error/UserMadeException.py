class TooHot(Exception):
    pass
class TooCold(Exception):
    pass
try:
    temperature = float(input("Enter the temperature: "))
    if temperature > 40:
        raise TooHot("It's too hot!")
    elif temperature < 20:
        raise TooCold("It's too cold!")
    else:
        print(f"The temperature is {temperature} degrees.")
except TooHot as e:
    print(f"Error: {e}")
except TooCold as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Invalid input. Please enter a numeric value for the temperature.")