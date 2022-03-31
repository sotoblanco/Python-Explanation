# Decorators

def hello(name="Pastor"):
    print("This hello() function has been exceuted!")

    def greet():
        return '\t This is the greet() function inside hello'

    def welcome():
        return '\t This is welcome() inside hello'

    print(greet())

    print(welcome())

    print("This is the end of the hello function!")


hello()


def hello(name="Pastor"):
    print("This hello() function has been exceuted!")

    def greet():
        return '\t This is the greet() function inside hello'

    def welcome():
        return '\t This is welcome() inside hello'

    print(greet())

    print(welcome())

    print("This is the end of the hello function!")


hello()

# return a function

def cool():
    def super_cool():
        return "I am very cool!"

    return super_cool


# function as argument
# we can execute a function by using as argument of another function
def hello():
    return "Hi!"


def other(some_def_func):
    print("Other code runs here!")
    print(some_def_func())

other(hello)










