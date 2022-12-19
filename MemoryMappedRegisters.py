class MemoryMappedRegisters:

    def __init__(self, rf):
        self.memMappedfile = [0]*5
        self.rf = rf


    def write_loadnoc(self, rs1, rs2, imm):
        x = imm//4
        self.memMappedfile[x] = self.rf.read_reg(rs2)

    def write_storenoc(self):
        self.memMappedfile[4] = 1

    def dump(self):
        return self.memMappedfile