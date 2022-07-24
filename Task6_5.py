"""
A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance.
Implement singleton logic inside your custom class using a method to initialize class instance.
"""

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class Sun():
    pass


if __name__ == '__main__':
    p = Sun()
    f = Sun()
    print(p is f)