class Student:
    def __init__(self, name):
        self.__name = name  # پرائیویٹ اٹریبیوٹ

    def get_name(self):  # پبلک میتھڈ
        return self.__name

s1 = Student("Mazhar")
print(s1.get_name())  # درست طریقہ: "Mazhar"
# print(s1.__name)  # یہ غلط ہے، کیونکہ __name پرائیویٹ ہے
