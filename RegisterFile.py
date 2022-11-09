from numpy import zeros

class RegisterFile:

    def __init__(self):
        self.regfile = list(zeros(32))
    
    def read_reg(self, reg):
        return self.regfile[reg]
    
    def write_reg(self, reg, val):
        self.regfile[reg] = val
    
    def dump(self):
        return self.regfile