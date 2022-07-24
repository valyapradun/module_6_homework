from collections import deque


class HistoryDict:
    """ Implement custom dictionary that will memorize 3 latest changed keys.
        Using method "get_history" return this keys.
    """

    def __init__(self, some_dict=None):
        if some_dict is not None:
            self.some_dict = some_dict
            self.de = deque(some_dict.keys(), 3)
        else:
            self.some_dict = {}
            self.de = deque([], 3)

    def set_value(self, key, value):
        self.some_dict[key] = value
        self.de.append(key)

    def get_history(self):
        print(self.some_dict)
        print(list(self.de))


if __name__ == '__main__':
    d0 = HistoryDict()
    d0.set_value("bar", 43)
    d0.set_value("foo", 1)
    d0.set_value("foo", 2)
    d0.set_value("bar", 55)
    d0.get_history()

    d1 = HistoryDict({"test1": 1, "test2": 2})
    d1.set_value("test3", 3)
    d1.set_value("test4", 4)
    d1.set_value("test5", 5)
    d1.get_history()
