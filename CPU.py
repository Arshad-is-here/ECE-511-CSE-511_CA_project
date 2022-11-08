from InstructionMemory import InstructionMemory
from DataMemory import DataMemory
from RegisterFile import RegisterFile

from Fetch import Fetch
from Decode import Decode
from Execute import Execute
from Memory import Memory
from WriteBack import WriteBack

class CPU:
    
    def __init__(self, binary, dMemLatency, dMemSize, iMemLatency, iMemSize):

        self.imem = InstructionMemory(access_delay=iMemLatency, size=iMemSize)
        self.dmem = DataMemory(access_latency=dMemLatency, size=dMemSize)
        self.rf = RegisterFile()
        self.F = Fetch(self.imem)
        self.D = Decode(self.rf)
        self.X = Execute()
        self.M = Memory(self.dmem)
        self.W = WriteBack()
        self.binary = binary
        self.PC = 0
    
    def initialize(self):
        self.imem.initialize(self.binary)


    def simulate(self):
        
        for cycle in range(1,100):

            # F -> D
            f2d = self.F.fetchToDecode()
            # D -> X
            d2x = self.D.decodeToExecute()
            # X -> M

            # M -> W

            # Fetch
            self.F.fetch(self.PC)
            # Decode
            (opcode_type, func, rd, rs1, rs2, offset) = self.D.decode()

            # Execute

            # Memory

            # WriteBack


