import random

NAME_1 = "COLEGIO"
NAME_2 = "MSFT"
NAME_3 = "GOOG"

ranges = dict()
ranges[NAME_1] = (-4.50, 6.00)
ranges[NAME_2] = (-5.00, 5.00)
ranges[NAME_3] = (-5.00, 5.00)

prev_prices = dict()


def get_share_price(investment_name):
    """Given a string investment_name, returns the current share price of the investment"""
    prev_price = (
        random.uniform(0.10, 10.00)
        if not (investment_name in prev_prices)
        else prev_prices[investment_name]
    )
    lower_bound = prev_price + ranges[investment_name][0]
    upper_bound = prev_price + ranges[investment_name][1]
    if lower_bound < 0:
        lower_bound = 0.01
    new_price = round(random.uniform(lower_bound, upper_bound), 2)
    prev_prices[investment_name] = new_price
    return new_price
