class Execute:
    #00000000010100000000000000010011
    
    def __init__(self,rf):
        self.rf = rf
        self.opcode_type = 0
        self.instruc = 0
        self.func = 0
        self.rs1 = 0
        self.rs2 = 0
        self.imm = 0
        self.offset = 0
        self.rd = 0

    def execute_compute(self,PC,D):
        (self.opcode_type, self.func, self.rd, self.rs1,self.rs2,self.offset) = D.decodeToExecute()

        if(D.opcode_type == 'R'):
            if(D.func == 'add'):
                self.rf[self.rd] = self.rf[self.rs1] + self.rf[self.rs2]
            
            if(D.func == 'sub'):
                self.rd = self.rs1- self.rs2
