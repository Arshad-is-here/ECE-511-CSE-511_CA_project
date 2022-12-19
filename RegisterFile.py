from numpy import zeros


class RegisterFile:

    """
    @brief      Represents the register file unit in the pipeline.
    """

    def __init__(self):

        """
        @brief      Contructor to instatiate the Register File
        @param      None
        @return     The register file
        """

        # The register file has been initialized with value 1 
        # so as to make the changes visible to the reader
        self.regfile = list(zeros(32))
        for i in range(32):
            self.write_reg(i, 1)

    def read_reg(self, reg):

        """
        @brief      Reads the value in the register
        @param      reg: the register to be read (0 to 31)
        @return     value stored in the register
        """

        return self.regfile[reg]

    def write_reg(self, reg, val):

        """
        @brief      Writes to a given register
        @param      reg: the register to be written to
        @param      val: the value to be written in reg
        @return     None
        """

        self.regfile[reg] = val

    def dump(self):

        """
        @brief      Dumps the register file to print its contents
        @param      None
        @return     the entire register file
        """

        return self.regfile