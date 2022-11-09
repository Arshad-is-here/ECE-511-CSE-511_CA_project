class Memory:

    def __init__(self, rf):
        self.rf = rf
        self.func = 0
        self.rd = 0
        self.x = 0
        self.pc = 0

    def writeback_compute(self, M):
        if M[0] != 0 or M[1] != 0 or M[2] != 0 or M[3] != 0:
            self.x = M[0]
            self.rd = M[1]
            self.pc = M[2]
            self.func = M[3]

        if self.func != "beq" or self.func != "sw":
            self.rf[self.rd] = self.x
