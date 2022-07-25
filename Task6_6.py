"""
Implement a class Money to represent value and currency.
You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition and subtraction).
Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates to your default currency
"""


class Money(object):
    """ Class Money to represent value and currency"""

    exchange_rate = {
        "USD": 1,
        "EUR": 0.97,
        "GBP": 0.83,
        "JPY": 136.09,
        "RUB": 58.12,
        "CNY": 6.75,
        "BYN": 3.37,
        "PLN": 4.64
    }

    def __init__(self, amount: float = 0, currency: str = "USD"):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        return Money(self.amount / self.exchange_rate[self.currency] + other.amount / other.exchange_rate[other.currency])

    def __sub__(self, other):
        return Money(self.amount / self.exchange_rate[self.currency] - other.amount / other.exchange_rate[other.currency])

    def __mul__(self, other):
        return Money(self.amount / self.exchange_rate[self.currency] * other.amount / other.exchange_rate[other.currency])

    def __truediv__(self, other):
        return Money(self.amount / self.exchange_rate[self.currency] / other.amount / other.exchange_rate[other.currency])

    def __lt__(self, other):
        if self.amount / self.exchange_rate[self.currency] < other.amount / other.exchange_rate[other.currency]:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.amount / self.exchange_rate[self.currency] > other.amount / other.exchange_rate[other.currency]:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.amount / self.exchange_rate[self.currency] == other.amount / other.exchange_rate[other.currency]:
            return True
        else:
            return False

    def __str__(self):
        return str(self.amount)# + " " + self.currency


if __name__ == '__main__':
    x = Money(10, "BYN")
    y = Money(11)
    z = Money(12.34, "EUR")
    print(z*0.2)
