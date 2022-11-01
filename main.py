

# Define your function here
def laps_to_miles(user_laps):
    return user_laps * .25

def in_class_activity1():
    laps = float(input("Please enter the amount of laps: "))

    print(f'{laps} is {laps_to_miles(laps):.2f} miles')


def in_class_activity2():
    mpg = float(input("Please input miles per gallon: "))
    gas_price = float(input("Please input gas price: "))

    print(f'{driving_cost(mpg,gas_price,10):.2f}')
    print(f'{driving_cost(mpg, gas_price, 50):.2f}')
    print(f'{driving_cost(mpg, gas_price, 400):.2f}')


def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return (miles_driven/miles_per_gallon)*dollars_per_gallon

# uncomment to run activity 1
#in_class_activity1()

# uncomment to run activity 2
#in_class_activity2()