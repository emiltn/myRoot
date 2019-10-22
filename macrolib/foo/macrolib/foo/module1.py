#print("Importing: foo.module1")
import numpy as np
import macrolib.bar

class MainClass(object):
    def __init__(self):
        print("Running: 'MainClass.__init__'")
        self.x = 0

    def __repr__(self):
        return "x = %d" % self.x

    def add(self):
        self.x +=1

    def sub(self):
        self.x -= 1

    def multiply(self, value):
        macrolib.bar.module1.multiply(self, value)




if __name__ == "__main__":
    print("Running as main: 'foo.module1'")


    o = MainClass()
    o.add()
    o.add()
    o.multiply(100)
    print(o)
