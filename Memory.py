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
        self.pc = -1
        self.instruction = ''

    def memory_compute(self, E):
        if E[0] != '' or E[1] != '' or E[2] != -1 or E[3] != '' or E[4] != '' or E[5] != '' or E[6] != '':
            self.x = E[0]
            self.rd = E[1]
            self.pc = E[2]
            self.offset = E[3]
            self.func = E[4]
            self.rs1 = E[5]
            self.rs2 = E[6]
            self.instruction = E[7]

            if self.func == "lw":
                self.x = self.dmem.read_data(self.rf.read_reg(self.rs1) + int(self.offset, 2))

            elif self.func == "sw":
                self.dmem.write_data(self.rf.read_reg(self.rs1) + int(self.offset, 2), self.rf.read_reg(self.rs2))

    def memoryToWriteback(self):
        return self.x, self.rd, self.pc, self.func, self.instruction