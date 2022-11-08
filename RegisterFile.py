from numpy import zeros

class RegisterFile:

    def __init__(self):
        self.regfile = list(zeros(32))
    
    def read_reg(self, reg):
        return self.regfile[reg]