from numpy import zeros

class RegisterFile:

    def __init__(self):
        self.regfile = dict()
    
    def initialize(self):
        self.regfile.keys = [bin(i)[2:] for i in range(32)]
        self.regfile.values = list(zeros(32))
    
    def read_reg(self, reg):
        return self.regfile[reg]