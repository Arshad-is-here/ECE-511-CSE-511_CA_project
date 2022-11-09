class Execute:

    def __init__(self, rf):
        self.rf= rf
        self.opcode_type = ''
        self.func = ''
        self.rs1 = ''
        self.rs2 = ''
        self.offset = ''
        self.rd = ''
        self.x = ''
        self.pc = ''
        self.instruction=''

    def execute_compute(self, D):
        #if D[0] != '' and D[1] != '' and D[2] != '' and D[3] != '' and D[4] != '' and D[5] != '' :
        if D[0] != '' or D[1] != '' or D[2] != '' or D[3] != '' or D[4] != '' or D[5] != '' :
            self.opcode_type = D[0]
            self.func = D[1]
            self.rd = D[2]
            self.rs1 = D[3]
            self.rs2 = D[4]
            self.offset = D[5]
            self.instruction=D[6]

            if self.opcode_type == 'R':
                #add
                if self.func == 'add':
                    self.x = self.rf.read_reg(self.rs1) + self.rf.read_reg(self.rs2)

                #sub
                elif self.func == 'sub':
                    self.x = self.rf.read_reg(self.rs1) + self.rf.read_reg(self.rs2)

                #sll
                elif self.func == 'sll':
                    self.x = self.rf.read_reg(self.rs1) << self.rf.read_reg(self.rs2)

                #sra
                elif self.func == 'sra':
                    self.x = self.rf.read_reg(self.rs1) >> self.rf.read_reg(self.rs2)

                #or
                elif self.func == 'or':
                    self.x = self.rf.read_reg(self.rs1) | self.rf.read_reg(self.rs2)

                #and
                elif self.func == 'and':
                    self.x = self.rf.read_reg(self.rs1) & self.rf.read_reg(self.rs2)

            elif self.opcode_type == 'I':
                #addi
                if self.func == "addi":
                    self.x = self.rf.read_reg(self.rs1) + int(self.offset, 2)

            elif self.opcode_type == 'SB':
                #beq
                if self.func == "beq":
                    if self.rf.read_reg(self.rs1) == self.rf.read_reg(self.rs2):
                        self.pc += self.offset

    def executeToMemory(self):
        return self.x, self.rd, self.pc, self.offset, self.func, self.rs1, self.rs2
