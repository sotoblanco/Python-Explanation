try:
    result = 10 + 10
except:
    print("There is a error on your code")

else:
    print("Add well!")
    print(result)

try:
    f = open('testfile', 'r')
    f.write("write a test line")
except TypeError:
    print("There was a type error!")

except OSError:
    print("Hey, you have an OS Error")
finally:
    print("I always run")


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("That's not a number: ")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("I will always run at the end")




ask_for_int()
    