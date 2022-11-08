class Execute:

    def __init__(self, rf):
        self.rf = rf
        self.opcode_type = 0
        self.func = 0
        self.rs1 = 0
        self.rs2 = 0
        self.imm = 0
        self.offset = 0
        self.rd = 0
        self.x = 0
        self.pc = 0

    def execute_compute(self, D):
        (self.opcode_type, self.func, self.rd, self.rs1, self.rs2, self.offset) = D.decodeToExecute()

        if self.opcode_type == 'R':
            #add
            if self.func == 'add':
                self.x = self.rf[self.rs1] + self.rf[self.rs2]

            #sub
            elif self.func == 'sub':
                self.x = self.rf[self.rs1] + self.rf[self.rs2]

            #sll
            elif self.func == 'sll':
                self.x = self.rf[self.rs1] << self.rf[self.rs2]

            #sra
            elif self.func == 'sra':
                self.x = self.rf[self.rs1] >> self.rf[self.rs2]

            #or
            elif self.func == 'or':
                self.x = self.rf[self.rs1] | self.rf[self.rs2]

            #and
            elif self.func == 'and':
                self.x = self.rf[self.rs1] & self.rf[self.rs2]

        elif self.opcode_type == 'I':
            #addi
            if self.func == "addi":
                self.x = self.rf[self.rs1] + int(offset, 2)

        elif self.opcode_type == 'SB':
            #beq
            if self.func == "beq":
                if self.rf[self.rs1] == self.rf[self.rs2]:
                    self.pc += self.offset

    def executetomemory(self):
        return self.x, self.rd, self.pc, self.offset, self.func, self.rs1, self.rs2

