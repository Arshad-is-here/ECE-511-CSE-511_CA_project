class Execute:

    """
    @brief      Describes the class attributes and functionalities of the eXecute stage.
    """

    def __init__(self, rf):

        """
        @brief      Constructor to instantiate an object of the eXecute stage
        @param      rf: register file (to read the values of rs1 and rs2)
        @return     The eXecute stage
        """

        self.rf= rf                     # initializing local register file
        self.opcode_type = ''           # initializing opcode type
        self.func = ''                  # initializing function of the instruction
        self.rs1 = ''                   # initializing source register 1
        self.rs2 = ''                   # initializing source register 2
        self.offset = ''                # initializing instruction offset
        self.rd = ''                    # initializing destination register
        self.x = ''                     # initializing value destinations
        self.pc = -1                    # initializing local program counter
        self.instruction = ''           # initializing instruction
        self.branchTaken = False        # initializing branch status

    def execute_compute(self, D, pc):

        """
        @brief      Executes the instruction received from the Decode stage
        @param      D: parameters received from the Decode stage
        @param      pc: program counter received from the CPU
        @return     None
        """

        # if the Decode stage wasn't empty
        if D[0] != '' or D[1] != '' or D[2] != '' or D[3] != '' or D[4] != '' or D[5] != '' :
            self.opcode_type = D[0]     # get the type of opcode
            self.func = D[1]            # get the functionality of the instruction
            self.rd = D[2]              # get the destination register
            self.rs1 = D[3]             # get source register 1
            self.rs2 = D[4]             # get source register 2
            self.offset = D[5]          # get instruction offset
            self.instruction = D[6]     # get the instruction (in binary)

            if self.opcode_type == 'R':     # if the instruction is R type

                if self.func == 'add':      # add
                    self.x = self.rf.read_reg(self.rs1) + self.rf.read_reg(self.rs2)

                elif self.func == 'sub':    # sub
                    self.x = self.rf.read_reg(self.rs1) - self.rf.read_reg(self.rs2)

                elif self.func == 'sll':    # sll
                    self.x = self.rf.read_reg(self.rs1) << self.rf.read_reg(self.rs2)
                
                elif self.func == 'sra':    # sra
                    self.x = self.rf.read_reg(self.rs1) >> self.rf.read_reg(self.rs2)

                elif self.func == 'or':     # or
                    self.x = self.rf.read_reg(self.rs1) | self.rf.read_reg(self.rs2)

                elif self.func == 'and':    # and
                    self.x = self.rf.read_reg(self.rs1) & self.rf.read_reg(self.rs2)

                self.pc = pc                # getting the program counter

            elif self.opcode_type == 'I':   # if the instruction is I type
                if self.func == "addi":     # addi
                    self.x = self.rf.read_reg(self.rs1) + int(self.offset, 2)
                self.pc = pc                # getting the program counter

            elif self.opcode_type == 'SB':  # if the instruction is SB type
                if self.func == "beq":      # beq
                    if self.rf.read_reg(self.rs1) == self.rf.read_reg(self.rs2):    # 'branch is taken' case
                        self.pc = int(self.offset, 2)
                        self.branchTaken = True
                    else:                                                           # 'branch is not taken' case
                        self.branchTaken = False
                        self.pc = pc          

    def executeToMemory(self):

        """
        @brief      Transfers the parameters from eXecute stage back to the CPU, where it will be passed on to Memory stage
        @param      None
        @return     list: all the parameters in eXecute stage
        """

        ret = [self.x, self.rd, self.pc, self.offset, self.func, self.rs1, self.rs2, self.instruction, self.branchTaken]
        self.instruction = ''
        return ret