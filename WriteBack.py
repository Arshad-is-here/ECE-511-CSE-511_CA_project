class WriteBack:

    def __init__(self, rf):
        self.rf = rf
        self.func = ''
        self.rd = ''
        self.x = ''
        self.pc = -1
        self.instruction = ''

    def writeback_compute(self, M):
        if M[0] != '' or M[1] != '' or M[2] != -1 or M[3] != '':
            self.x = M[0]
            self.rd = M[1]
            self.pc = M[2]
            self.func = M[3]
            self.instruction = M[4]
            if self.rd != "":
                self.rf.write_reg(self.rd, self.x)

    def write_Back(self):
        print(self.rf.dump())
        return self.rf