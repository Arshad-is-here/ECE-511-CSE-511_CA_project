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
        text = open('log.txt', 'w')
        for cycle in range(1, len(self.imem.dump()) + 8):

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

            text.write("---------------------------------------------\n")
            text.write("Clock cycle is: {}\n".format(cycle))
            text.write('Fetch: {}\n'.format(self.F.instruction))
            text.write('Decode: {}\n'.format(self.D.instruction))
            text.write('Execute: {}\n'.format(self.X.instruction))
            text.write('Memory: {}\n'.format(self.M.instruction))
            text.write('WriteBack: {}\n'.format(self.W.instruction))

            if cycle < 5 + len(self.imem.dump()):
                text.write('Fetch: {}\n'.format(self.F.instruction))
                text.write('Decode: {}\n'.format(self.D.instruction))
                text.write('Execute: {}\n'.format(d2x))
                text.write('Memory: {}\n'.format(x2m))
                text.write('WriteBack: {}\n'.format(m2w))
                text.write('Register File: {}\n'.format(self.rf.dump()))

            print("Clock cycle is: {}".format(cycle))
            print('Fetch: {}'.format(self.F.instruction))
            print('Decode: {}'.format(self.D.instruction))
            print('Execute: {}'.format(self.X.instruction))
            print('Memory: {}'.format(self.M.instruction))
            print('WriteBack: {}'.format(self.W.instruction))

        text.write("Memory state is: {}\n".format(self.dmem.dump()))
        text.close()

        print('RF dump from CPU')
        print(self.rf.dump())


system = CPU('testfile.txt', 0, 512, 0, 512)
system.initBinary()
system.simulate()