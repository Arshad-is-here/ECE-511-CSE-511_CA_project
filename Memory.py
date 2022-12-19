class Memory:

    """
    @brief      Describes the class attributes and functionalities of the Memory stage.
    """

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

    def memory_compute(self, E, mapped):

        """
        @brief      Performs the memory operations (load and store)
        @param      E: parameters received from the eXecute stage
        @return     None
        """

        # check if the eXecute stage was not empty
        if E[0] != '' or E[1] != '' or E[2] != -1 or E[3] != '' or E[4] != '' or E[5] != '' or E[6] != '':
            self.x = E[0]               
            self.rd = E[1]              # get the destination register
            self.pc = E[2]              # get the program counter
            self.offset = E[3]          # get the instruction offset
            self.func = E[4]            # get the instruction functionality
            self.rs1 = E[5]             # get source register 1
            self.rs2 = E[6]             # get source register 2
            self.instruction = E[7]     # get the instruction

            if self.func == "lw":       # handling loads
                self.x = self.dmem.read_data(self.rf.read_reg(self.rs1) + int(self.offset, 2))

            elif self.func == "sw":     # handling stores
                self.dmem.write_data(self.rf.read_reg(self.rs1) + int(self.offset, 2), self.rf.read_reg(self.rs2))

            elif self.func == "LOADNOC":
                mapped.write_reg(self.rs1, self.rs2, int(self.offset, 2))
                print("Hii")

            elif self.func == "STORENOC":
                mapped.write_re(16)
                mapped.dump()

        return mapped

    def memoryToWriteback(self):

        """
        @brief      Transfers the parameters from Memory stage back to the CPU, where it will be passed on to Writeback stage
        @param      None
        @return     list: all the parameters in Memory stage
        """

        return [self.x, self.rd, self.pc, self.func, self.instruction, self.rs1, self.rs2]