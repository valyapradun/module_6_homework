class Counter:
    """ Implement a Counter class which optionally accepts the start value and the counter stop value.
        If the start value is not specified the counter should begin with 0.
        If the stop value is not specified it should be counting up infinitely.
        If the counter reaches the stop value, print "Maximal value is reached."
        Implement to methods: "increment" and "get"
    """

    def __init__(self, start=0, stop=float('inf')):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.start < self.stop:
            self.start += 1
            return self.start
        else:
            print('Maximal value is reached.')

    def get(self):
        print(self.start)


if __name__ == '__main__':
    c = Counter(start=42)
    c.increment()
    c.get()

    c = Counter()
    c.increment()
    c.get()
    c.increment()
    c.get()

    c = Counter(start=42, stop=43)
    c.increment()
    c.get()
    c.increment()
    c.get()
