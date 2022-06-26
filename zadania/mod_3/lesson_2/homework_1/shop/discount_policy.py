
def default_policy(total_price):
    return total_price


def loyal_consumer_policy(total_price):
    return 0.95 * total_price


def christmas_policy(total_price):
    if total_price > 100:
        return total_price - 20
    return total_price
