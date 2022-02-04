
x = 25

# LEGB Rule
# Local
# Enclosing
# Global
# Buitl in

name = "This is a global string"
def greet():
    # enclosing
    name = "Sammy"

    def hello():
        # Local
        name = "I am local"
        print("Hello "+ name)


greet()

x = 50

def func():
    global x
    print(f'X is {x}')

    # LOCAL REASSIGNMENT ON A VAIRBALE

    x = "NEW VALUE"

    print('I just locally changed global')
    return x











    





