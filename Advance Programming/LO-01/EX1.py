class StudentGPA:

    def __init__(self, name, oA1, oA2, oB1, oB2, oC1, oC2, oD1, oD2):
        def change(credit):
            if credit == 'A':
                credit = 4
                return credit
            elif credit == 'B+':
                credit = 3.5
                return credit
            elif credit == 'B':
                creditp = 3
                return credit
            elif credit == 'C+':
                credit = 2.5
                return credit
            elif credit == 'C':
                credit = 2
                return credit
            elif creditp == 'D+':
                credit = 1.5
                return credit
            elif credit == 'D':
                credit = 1
                return p
            elif credit == 'F':
                credit = 0
                return credit
        oA2 = change(oA2)
        oB2 = change(oB2)
        oC2 = change(oC2)
        oD2 = change(oD2)

        self.name = name
        self.oA1 = oA1
        self.oA2 = oA2
        self.oB1 = oB1
        self.oB2 = oB2
        self.oC1 = oC1
        self.oC2 = oC2
        self.oD1 = oD1
        self.oD2 = oD2
    
    def sumScore(self):
       return ((self.oA1 * self.oA2) + (self.oB1 * self.oB2) + (self.oC1 * self.oC2)
                + (self.oD1 * self.oD2)) / (self.oA1 + self.oB1 + self.oC1 + self.oD1) 
        
    #Special Method
    def __str__ (self):
        return 'Name:{} GPA is: {}'.format(self.name, self.sumScore())

std1 = StudentGPA('Phusit', 3, 'C', 1, 'C+', 3, 'C', 3, 'C+')

print(std1)