class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    @staticmethod   
    def hello():
        print("hello")    
        
    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("hi",self.name,"your avg score is:",sum/3)   
       
s1 = Student("subhan", [77,78,79])
s1.get_avg()
s1.hello()


