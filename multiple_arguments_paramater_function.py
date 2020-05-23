
def fooOneStar(first, second, third, *one):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all param %s" % list(one))

def barTwoStar(first, second, third, **param):
     print(param["action"])

def get_follow(self, **parameters):
    self.get_only_page(**parameters)

def get_only_page(self, **parameters):
    self.to_comment = parameters["to_comment"]
    self.webdriver.get(parameters["share_link"])

fooOneStar(1,2,3,4,5)
barTwoStar(1, 2, 3, action = "sum", number = "first")
get_follow(share_link= "https://www.instagram.com/test", to_comment= "mest")