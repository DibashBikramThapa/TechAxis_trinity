def test(*args, **kwargs):
    # args used for pass by value
    print(args[0])
    # kwargs used for pass by reference
    print(kwargs.get('my_list'))

my_list = [1,2,3]
kwargs = {'my_list': my_list}
test(1, **kwargs)


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("I am from Animal")

animal = Animal('Dog', 12)
animal.run()

class Cat(Animal):

    def run(self):
        # Call the parent func
        super().run()
        print("I am from cat")

cat = Cat('Cat', 23)
cat.run()

def validate_param(func):
    # use a func named wrapper or any name to collect the variable send in 'func' using args and kwargs.
    def wrapper(*args, **kwargs):
        print('args: ', args)
        a = args[0]
        b = args[1]
        # two way to check type, one is using type(a) or isinstance(a, int)
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("a,b should be int or float")
        val = func(a, b)
        # print the result in val
        print(val)
    return wrapper

@validate_param
def add(a, b):
    return a+ b

add(1, 2)
add(1, '2')
