def func(x):


        def func1():


                print("Decorated")


                x()


        func1()


def func2():


        print("Ordinary")


p = func(func2)
