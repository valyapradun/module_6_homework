"""
Implement a class Money to represent value and currency.
You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition and subtraction).
Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates to your default currency
"""


class Money(object):
    """ Class Money to represent value and currency"""

    exchange_rate = {
        "USD": 1,
        "EUR": 0.93,
        "GBP": 0.83,
        "JPY": 130.84,
        "RUB": 58.12,
        "CNY": 6.75,
        "BYN": 2.1,
        "PLN": 4.64
    }

    def __init__(self, amount: float = 0, currency: str = "USD"):
        self.amount_usd = amount / self.exchange_rate[currency]
        self.currency = currency

    def __add__(self, other):
        return Money((self.amount_usd + other.amount_usd) * self.exchange_rate[self.currency], self.currency)

    def __radd__(self, other):
        if isinstance(other, int):
            return Money((self.amount_usd + other) * self.exchange_rate[self.currency], self.currency)
        else:
            self.__add__(other)

    def __sub__(self, other):
        return Money((self.amount_usd - other.amount_usd) * self.exchange_rate[self.currency], self.currency)

    def __mul__(self, other):
        if isinstance(other, float):
            return Money(self.amount_usd * other * self.exchange_rate[self.currency], self.currency)
        else:
            return Money(self.amount_usd * other.amount_usd * self.exchange_rate[self.currency], self.currency)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return Money(self.amount_usd / other.amount_usd * self.exchange_rate[self.currency], self.currency)

    def __lt__(self, other):
        return self.amount_usd < other.amount_usd

    def __le__(self, other):
        return self.amount_usd <= other.amount_usd

    def __gt__(self, other):
        return self.amount_usd > other.amount_usd

    def __ge__(self, other):
        return self.amount_usd >= other.amount_usd

    def __eq__(self, other):
        return self.amount_usd == other.amount_usd

    def __ne__(self, other):
        return self.amount_usd != other.amount_usd

    def __str__(self):
        return str(self.amount_usd * self.exchange_rate[self.currency]) + " " + self.currency


if __name__ == '__main__':
    x = Money(10, "BYN")
    y = Money(11)
    z = Money(12.34, "EUR")
    print(x > y)
    print(x + y)
    print(3.11 * x)
    print(y * 0.8)
    print(z + 3.11 * x + y * 0.8)

    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
    s = sum(lst)
    print(s)
