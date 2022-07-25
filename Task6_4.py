"""
Create hierarchy out of birds. 
Implement 4 classes:
* class `Bird` with an attribute `name` and methods `fly` and `walk`.
* class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value. 
Implement the method `eat` which will describe its typical ration.
* class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
* class `SuperBird` which can do all of it: walk, fly, swim and eat.
But be careful which "eat" method you inherit.

Implement str() function call for each class.

"""


class Bird:
    """ Class `Bird` with an attribute `name` and methods `fly` and `walk`"""

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(self.name + ' bird can fly')

    def walk(self):
        print(self.name + ' bird can walk')

    def __str__(self):
        return f'{self.name} bird can fly and walk'


class FlyingBird(Bird):
    """ class `FlyingBird` with attributes `name`, `ration`, and with the same methods (fly, walk).
        `ration` must have default value.
        Implement the method `eat` which will describe its typical ration.
    """

    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print('It eats mostly ' + self.ration)

    def __str__(self):
        return super().__str__() + ' and eat'


class NonFlyingBird(Bird):
    """ class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
        Add same "eat" method but with other implementation regarding the swimming bird tastes.
    """

    def __init__(self, name, ration='fish'):
        self.name = name
        self.ration = ration

    def eat(self):
        print('NonFlyingBird eats mostly ' + self.ration)

    def swim(self):
        print(self.name + ' bird can swim')

    def fly(self):
        print(f'AttributeError: "{self.name}" object has no attribute "fly"')

    def __str__(self):
        return f'{self.name} bird can walk, swim and eat'


class SuperBird(NonFlyingBird, FlyingBird):
    """ class `SuperBird` which can do all of it: walk, fly, swim and eat.
        But be careful which "eat" method you inherit.
    """
    def __str__(self):
        return f'{self.name} bird can fly, walk, swim and eat'


if __name__ == '__main__':
    b = Bird('Any')
    b.walk()
    print(b)

    p = NonFlyingBird('Penguin', 'fish')
    p.swim()
    p.fly()
    p.eat()
    print(p)

    c = FlyingBird("Canary")
    print(c)
    c.eat()

    s = SuperBird("Gull")
    print(s)
    print(SuperBird.__mro__)
    s.eat()