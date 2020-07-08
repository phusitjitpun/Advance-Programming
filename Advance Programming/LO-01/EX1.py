class StudentGPA:
    def __init__(self, name, ob1, ob2):
        self.name = name
        self.oA1 = oA1
        self.oA2 = oA2
        self.oB3 = oB3
        self.oB4 = oB4
        self.oC5 = oC5
        self.oC6 = oC6
        self.oD7 = oD7
        self.oD8 = oD8

    def sumScore(self):
        return self.score2 / self.score1
          
    #def sumScore1():
        #return sum.sumScore1()

    #def sumScore2():
        #return sumScore1 / 10

    #Special Method
    def __str__ (self):
        return 'Name:{}, GPA is: {}'.format(self.name, self.sumScore())


std1 = StudentGPA('Phusit', 10, 22.5)
'''std2 = StudentGPA('Elec LAB', 1, 2.5)
std3 = StudentGPA('Problem', 3, 2.0)
std4 = StudentGPA('Healthy', 3, 2.5)'''

print(std1)