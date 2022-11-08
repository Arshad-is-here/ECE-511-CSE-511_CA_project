from InstructionMemory import InstructionMemory
from DataMemory import DataMemory
from RegisterFile import RegisterFile

from Fetch import Fetch
from Decode import Decode
from Execute import Execute
from Memory import Memory
from WriteBack import WriteBack

class CPU:
    
    def __init__(self):
        self.imem = InstructionMemory(size=2**30)
        self.dmem = DataMemory(size=2**30)
        self.rf = RegisterFile()
        self.F = Fetch(self.imem)
        self.D = Decode(self.rf)
        self.X = Execute()
        self.M = Memory(self.dmem)
        self.W = WriteBack()
    
    def 