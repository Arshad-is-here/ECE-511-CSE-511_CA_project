class WriteBack:

    """
    @brief      Describes the class attributes and functionalities of the Writeback stage.
    """

    def __init__(self, rf):

        """
        @brief      Constructor to instantiate an object of the Writeback stage
        @param      rf: register file (to write to rd)
        @return     The Writeback stage
        """

        self.rf = rf                # initializing local register file object
        self.func = ''              # initializing instruction functionality
        self.rd = ''                # initializing destination register
        self.x = ''                 # initializing value to store in rd
        self.pc = -1                # initializing program counter
        self.instruction = ''       # initializing instruction

    def writeback_compute(self, M):

        """
        @brief      Performs the writeback operation
        @param      M: parameters from the Memory stage
        @return     None
        """

        # check if the Memory stage wasn't empty
        if M[0] != '' or M[1] != '' or M[2] != -1 or M[3] != '':
            self.x = M[0]                               # getting the value for rd
            self.rd = M[1]                              # getting rd
            self.pc = M[2]                              # getting program counter
            self.func = M[3]                            # getting intruction functionality
            self.instruction = M[4]                     # getting the instruction
            if self.rd != "":                           # if rd is valid
                self.rf.write_reg(self.rd, self.x)      # write x to rd

    def write_Back(self):

        """
        @brief      Gives back the updated register file to the CPU
        @param      None
        @return     rf: updated register file
        """

        return self.rf