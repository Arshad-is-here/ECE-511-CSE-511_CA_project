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
        self.D = Decode()
        self.X = Execute(self.rf)
        self.M = Memory(self.rf, self.dmem)
        self.W = WriteBack(self.rf)
        self.binary = binary
        self.PC = -1
        self.branchTaken = False

    def initBinary(self):
        self.imem.initialize(self.binary)

    def simulate(self):

        for cycle in range(1, 10):

            # pass on to next stages
            f2d = self.F.fetchToDecode()  # F -> D
            d2x = self.D.decodeToExecute()  # D -> X
            x2m = self.X.executeToMemory()  # X -> M
            m2w = self.M.memoryToWriteback()  # M -> W
            self.rf = self.W.write_Back()

            self.branchTaken = x2m[-1]

            if self.branchTaken:
                self.PC = x2m[2]
                self.branchTaken = False
            else:
                self.PC = self.PC + 1

            # run the pipeline stages
            if self.PC < len(self.imem.dump()):
                self.F.fetch(self.PC)
            else:
                self.F.instruction = ''

            self.D.decode(f2d)
            self.X.execute_compute(d2x, self.PC)
            self.M.memory_compute(x2m)
            self.W.writeback_compute(m2w)

            print('Cycle: {}'.format(cycle))
            print('Fetch: {}'.format(self.F.instruction))
            print('Decode: {}'.format(self.D.instruction))
            # print('Execute: {}'.format(d2x))

        print('RF dump from CPU')
        print(self.rf.dump())


system = CPU('testfile.txt', 0, 512, 0, 512)
system.initBinary()
system.simulate()
