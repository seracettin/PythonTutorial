def decorator1(x):


        def f1(a, b):


                print("hello")


                if b==0:


                        print("NO")


                        return


                return decorator1(a, b)


        return f1


@decorator1

def decorator1(a, b):


        return a%b


decorator1(4,0)

decorator1(4,2)
