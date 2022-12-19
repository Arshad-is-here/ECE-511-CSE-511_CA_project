class Memory:

    """
    @brief      Describes the class attributes and functionalities of the Memory stage.
    """

    def __init__(self, rf, dmem):

        """
        @brief      Constructor to instantiate an object of the Memory stage
        @param      rf: register file (to read the values of rs1 and rs2)
        @param      dmem: data memory
        @return     The eXecute stage
        """

        self.rf = rf                # initializing local register file object
        self.dmem = dmem            # initializing local data memory object
        self.func = ''              # initializing the functionality of instruction
        self.rs1 = ''               # initializing source register 1
        self.rs2 = ''               # initializing source register 2
        self.offset = ''            # initializing instruction offset
        self.rd = ''                # initializing destination register
        self.x = ''                 # initializing value for destinations
        self.pc = -1                # initializing local program counter value
        self.instruction = ''       # initializing instruction

    def memory_compute(self, E):

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

    def memoryToWriteback(self):

        """
        @brief      Transfers the parameters from Memory stage back to the CPU, where it will be passed on to Writeback stage
        @param      None
        @return     list: all the parameters in Memory stage
        """

        return [self.x, self.rd, self.pc, self.func, self.instruction, self.rs1, self.rs2]