class InstructionMemory:

    """
    @brief      Represents the instruction memory unit in the pipeline.
    """

    def __init__(self, access_delay=1, size=512):

        """
        @brief      Constructor to instantiate instruction memory
        @param      access_latency: read/write latency of instruction memory memory | default: 1
        @param      size: size of instruction memory | default: 512 x 4B
        """

        self.access_delay = access_delay        # initializing access delay
        self.size = size                        # initializing size
        self.mem = ['' for _ in range(size)]    # initializing the memory with empty instructions

    def initialize(self, filepath):

        """
        @brief      Initializes the instruction memory with the instructions from the test binary
        @param      filepath: path to the test binary
        @return     None
        """

        instr = open(filepath, 'r')
        self.mem = instr.readlines()

    def read_instr(self, addr):

        """
        @brief      Performs read operation at a given address
        @param      addr: address to be read (given by PC)
        @return     instruction at addr
        """

        return self.mem[addr]

    def dump(self):

        """
        @brief      Dumps the instruction memory to get printed
        @param      None
        @return     the entire instruction memory
        """

        return self.mem