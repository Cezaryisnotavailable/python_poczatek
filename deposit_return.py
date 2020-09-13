import math

def return_on_investment (amount, rate, time):
    return amount * math.pow((1 + rate/100), time)