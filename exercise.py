class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introducing(self):
        print("Hi, I'm " + self.name, "I'm " + self.color)

    def is_it_red(self):
        if self.color == "red":
            return True
        else:
            return False

r1 = Robot("Tom", "blue", 30)
r2 = Robot("Jecky", "red", 40)
r1.introducing()
print(r1.is_it_red())