
def fooOneStar(first, second, third, *one):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all param %s" % list(one))

def barTwoStar(first, second, third, **param):
     print(param["action"])


fooOneStar(1,2,3,4,5)
barTwoStar(1, 2, 3, action = "sum", number = "first")