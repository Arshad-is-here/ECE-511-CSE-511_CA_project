class Memory:

    def __init__(self, rf, dmem):
        self.rf = rf
        self.dmem = dmem
        self.func = 0
        self.rs1 = 0
        self.rs2 = 0
        self.offset = 0
        self.rd = 0
        self.x = 0
        self.pc = 0

    def memory_compute(self, E):
        if E[0] != 0 or E[1] != 0 or E[2] != 0 or E[3] != 0 or E[4] != 0 or E[5] != 0 or E[6] != 0:
            self.x = E[0]
            self.rd = E[1]
            self.pc = E[2]
            self.offset = E[3]
            self.func = E[4]
            self.rs1 = E[5]
            self.rs2 = E[6]

            if self.func == "lw":
                self.x = dmem[self.rf[self.rs1] + int(self.offset, 2)]

            elif self.func == "sw":
                dmem[self.rf[self.rs1] + int(self.offset, 2)] = self.rf[self.rs2]

    def memorytowriteback(self):
        return self.x, self.rd, self.pc, self.func
