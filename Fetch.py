class Fetch:

    """
    @brief      Describes the class attributes and functionalities of the Fetch stage.
    """

    def __init__(self, imem):

        """
        @brief      Constructor to instantiate an object of the Fetch stage
        @param      imem: instruction memory
        @return     The Fetch stage
        """

        self.instruction = ''       # initializing the instruction
        self.imem = imem            # initializing local instruction memory object
        self.isStalled = False      # initializing stall status of Fetch

    def fetch(self, PC):

        """
        @brief      Fetches the instruction at a given program counter value
        @param      PC: program counter (from CPU)
        @return     None
        """

        self.instruction = self.imem.read_instr(PC) # fetch the instruction at PC

    def fetchToDecode(self):

        """
        @brief      Transfers the data from Fetch stage back to the CPU, where it will be passed on to Decode stage
        """

        return self.instruction


