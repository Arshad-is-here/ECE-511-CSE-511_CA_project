class Memory:

    def __init__(self, rf, dmem):
        self.rf = rf
        self.dmem = dmem
        self.func = ''
        self.rs1 = ''
        self.rs2 = ''
        self.offset = ''
        self.rd = ''
        self.x = ''
        self.pc = ''

    def memory_compute(self, E):
        if E[0] != '' and E[1] != '' and E[2] != '' and E[3] != '' and E[4] != '' and E[5] != '' and E[6] != '':
            self.x = E[0]
            self.rd = E[1]
            self.pc = E[2]
            self.offset = E[3]
            self.func = E[4]
            self.rs1 = E[5]
            self.rs2 = E[6]

            if self.func == "lw":
                self.x = self.dmem[self.rf.read_reg(self.rs1) + int(self.offset, 2)]

            elif self.func == "sw":
                self.dmem[self.rf.read_reg(self.rs1) + int(self.offset, 2)] = self.rf.read_reg(self.rs2)

    def memoryToWriteback(self):
        return self.x, self.rd, self.pc, self.func