class Greeter:
    def __init__(self, who):
        self.who = who

    def greet(self):
        return "Hello, %s!" % self.who