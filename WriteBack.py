class WriteBack:

    def __init__(self, rf):
        self.rf = rf
        self.func = ''
        self.rd = ''
        self.x = ''
        self.pc = ''

    def writeback_compute(self, M):
        if M[0] != '' and M[1] != '' and M[2] != '' and M[3] != '':
            self.x = M[0]
            self.rd = M[1]
            self.pc = M[2]
            self.func = M[3]

            
            self.rf.write_reg(self.rd, self.x)
            print(self.rf.dump())

        return self.rf