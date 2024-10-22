# print(1 + 2)
# print(type(1))
# print("mazhar" + "abbas")
# print(type("mazhar"))
# print([1, 2, 3,] + [4, 5, 6])
# print(type([1, 2, 3]))

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
        
    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal, newimg)
        

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()






















