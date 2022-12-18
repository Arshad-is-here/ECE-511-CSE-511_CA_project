from numpy import zeros


class DataMemory:

    """
    @brief      Represents the data memory unit in the pipeline.
    """

    def __init__(self, access_latency=1, size=512):

        """
        @brief      Constructor to instantiate data memory
        @param      access_latency: read/write latency of data memory | default: 1
        @param      size: size of data memory | default: 512
        """

        self.access_latency = access_latency    # initialize access_latency
        self.size = size                        # initialize size
        self.mem = zeros(size)                  # initialize memory with all zeros

    def read_data(self, raddr):

        """
        @brief      Reads and returns data from a given memory location
        @param      raddr: read address
        @return     data value present at raddr
        """

        return self.mem[raddr]

    def write_data(self, waddr, wdata):

        """
        @brief      Writes data to a given memory location
        @param      waddr: write address
        @param      wdata: write data
        @return     None
        """

        self.mem[waddr] = wdata

    def dump(self):

        """
        @brief      Dumps the entire data memory
        @param      None
        @return     the entire data memory
        """

        return self.mem