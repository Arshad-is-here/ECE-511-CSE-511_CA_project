import numpy as np
import matplotlib.pyplot as plt

from InstructionMemory import InstructionMemory
from DataMemory import DataMemory
from RegisterFile import RegisterFile
from MemoryMappedRegisters import MemoryMappedRegisters
from Fetch import Fetch
from Decode import Decode
from Execute import Execute
from Memory import Memory
from WriteBack import WriteBack


class CPU:
    """
    @brief      This class is a wrapper of the entire 5-stage pipeline designed. It ecapsulates
                the instances of the fetch, decode, execute, memory, and writeback stages along
                with data memory, instruction memory, and register file.
    """

    def __init__(self, binary, dMemLatency, dMemSize, iMemLatency, iMemSize):

        """
        @brief      Constructor for CPU class.
        @param      binary: the test binary.
        @param      dMemLatency: data memory latency.
        @param      dMemSize: data memory size.
        @param      iMemLatency: instruction memory latency.
        @param      iMemSize: instruction memory size.
        @return     None.
        """

        self.imem = InstructionMemory(access_delay=iMemLatency, size=iMemSize)  # initiating instruction memory
        self.iMemLatency = iMemLatency
        self.dmem = DataMemory(access_latency=dMemLatency, size=dMemSize)  # initiating data memory
        self.rf = RegisterFile()  # initiating register file
        self.mapped = MemoryMappedRegisters(self.rf)  # initializing memory mapped registers
        self.F = Fetch(self.imem)  # initiating fetch stages
        self.D = Decode()  # initiating decode stage
        self.X = Execute(self.rf)  # initiating execute stage
        self.M = Memory(self.rf, self.dmem)  # initiating memory stage
        self.W = WriteBack(self.rf)  # initiating writeback stage
        self.binary = binary  # initiating the test binary
        self.PC = 0  # initiating program counter
        self.branchTaken = False  # initiating branch status

    def initBinary(self):

        """
        @brief      Initializes the instruction memory with the contents
                    of the test binary file.
        @param      None.
        @return     None.
        """

        self.imem.initialize(self.binary)

    def simulate(self):

        """
        @brief      Simulates the 5-stage pipeline and stores the CPU timeline in log.txt.
        @param      None.
        @return     None.
        """

        text = open('log.txt', 'w')  # opening log.txt in write mode
        text1 = open('instruction_memory.txt', 'w')
        text4 = open('data_memory.txt', 'w')
        text.write(
            'NOTE: The register file has been initialized with value 1 so as to make the changes visible to the reader\n')

        nStalls = 0
        x = self.iMemLatency + 1
        for cycle in range(1, 50):

            # Each iteration of the loop is considered as a single clock cycle. The
            # first step in every cycle is to transfer the instructions from their
            # previous stage to the next stage. This is followed by processing the
            # transfered results in their new stages. Finally, we write the current
            # state of the pipeline in log.txt

            # pass on to next stages
            f2d = self.F.fetchToDecode()  # Fetch -> Decode
            d2x = self.D.decodeToExecute()  # Decode -> eXecute
            x2m = self.X.executeToMemory()  # eXecute -> Memory
            m2w = self.M.memoryToWriteback()  # Memory -> Writeback
            self.rf = self.W.write_Back()  # update the RF using data from writeback stage

            if ('' not in [self.X.rd, self.D.rd, self.D.rs1, self.D.rs2]):
                # STALL LOGIC FOR DECODE
                if (self.X.rd in [self.D.rd, self.D.rs1, self.D.rs2]) and self.W.rd not in [self.D.rd, self.D.rs1,
                                                                                            self.D.rs2]:
                    self.D.isStalled = True
                    d2x[0] = ''
                    d2x[1] = ''
                    d2x[2] = ''
                    d2x[3] = ''
                    d2x[4] = ''
                    d2x[5] = ''
                elif (self.M.rd in [self.D.rd, self.D.rs1, self.D.rs2]) and self.W.rd not in [self.D.rd, self.D.rs1,
                                                                                              self.D.rs2]:
                    self.D.isStalled = True
                    d2x[0] = ''
                    d2x[1] = ''
                    d2x[2] = ''
                    d2x[3] = ''
                    d2x[4] = ''
                    d2x[5] = ''
                else:
                    self.D.isStalled = False

                # STALL LOGIC FOR FETCH
                if self.D.isStalled:
                    self.F.isStalled = True
                    nStalls += 1
                else:
                    self.F.isStalled = False

            self.branchTaken = x2m[-1]  # update branch status

            if self.branchTaken:  # if branch taken
                self.PC = x2m[2]  # update PC to the target instruction
                self.branchTaken = False  # reset branch status in the CPU
                self.X.branchTaken = False  # reset branch status in the eXecute stage
                f2d = ''  # kill the instruction in Fetch
                d2x[-1] = ''  # kill the instruction in Decode
            else:
                if not self.F.isStalled and cycle % x == 0:
                    self.PC = self.PC + 1  # else, move PC to next instruction
                else:
                    f2d = ''

            # run the pipeline stages
            if not self.F.isStalled:
                if self.PC < len(self.imem.dump()):  # if instruction memory is not exhausted
                    self.F.fetch(self.PC)  # fetch new instruction
                else:
                    self.F.instruction = ''  # else, stop fetching new instruction

            if not self.D.isStalled:
                self.D.decode(f2d)  # run the decode stage
            self.X.execute_compute(d2x, self.PC)  # run the execute stage
            self.mapped = self.M.memory_compute(x2m, self.mapped)  # run the memory stage
            self.W.writeback_compute(m2w)  # run the writeback stage

            # Write the current state of the pipeline to the log file (log.txt)
            text.write("---------------------------------------------\n")
            text.write("Clock cycle is: {}\n".format(cycle))
            if self.F.instruction != '':
                text1.write("{} {}\n".format(cycle, self.imem.mem.index(self.F.instruction) + 1))
                text.write(
                    'Fetch: I{} -> {}\n'.format(self.imem.mem.index(self.F.instruction) + 1, self.F.instruction[:-1]))
            else:
                text.write('Fetch: \n')

            if self.D.instruction != '':
                text.write(
                    'Decode: I{} -> {}\n'.format(self.imem.mem.index(self.D.instruction) + 1, self.D.instruction[:-1]))
            else:
                text.write('Decode: \n')

            if self.X.instruction != '':
                text.write(
                    'Execute: I{} -> {}\n'.format(self.imem.mem.index(self.X.instruction) + 1, self.X.instruction[:-1]))
            else:
                text.write('Execute: \n')

            if self.M.instruction != '':
                if self.M.instruction[-8:-1] == '0000011' or self.M.instruction[-8:-1] == '0100011':
                    text4.write("{} {}\n".format(cycle, self.imem.mem.index(self.M.instruction) + 1))
                text.write(
                    'Memory: I{} -> {}\n'.format(self.imem.mem.index(self.M.instruction) + 1, self.M.instruction[:-1]))
            else:
                text.write('Memory: \n')

            if self.W.instruction != '':
                text.write('WriteBack: I{} -> {}\n'.format(self.imem.mem.index(self.W.instruction) + 1,
                                                           self.W.instruction[:-1]))
            else:
                text.write('WriteBack: \n')

            # Dumping the Register File at the end of each clock cycle
            text.write('Register File: {}\n'.format(self.rf.dump()))
            # Dumping the Memory Mapped Register File at the end of each clock cycle
            text.write('Memory Mapped Register File: {}\n'.format(self.mapped.dump()))

        # Dumping the data memory at the end of the program execution
        text.write("Ending data memory state is: {}\n".format(self.dmem.dump()))
        # Writing the number of stalls
        text.write("Number of clock cycles stalled in program: {}\n".format(nStalls))
        text.close()


system = CPU('testfile.txt', 0, 512, 2, 512)
system.initBinary()
system.simulate()

text2 = open('numbers.txt', 'r')
nums = text2.readlines()
data = {'Register instructions': (int)(nums[0]), 'Memory Instructions': (int)(nums[1])}
Instruction_Type = list(data.keys())
Number_of_instructions = list(data.values())
fig = plt.figure(figsize=(8, 5))
plt.bar(Instruction_Type, Number_of_instructions, color='orange', width=0.4)
plt.xlabel("Instruction Type")
plt.ylabel("Number of instructions")
plt.title("Number of Register and memory instructions")
plt.show()
text2.close()

text3 = open('instruction_memory.txt', 'r')
nums1 = text3.readlines()
cycles = []
inst_num = []
i = 0
for i in range(len(nums1)):
    j = 0
    while (nums1[i][j] != ' '):
        j += 1
    x = nums1[i][0:j]
    cycles.append((int)(x))
    y = nums1[i][j:len(nums1[i]) - 1]
    inst_num.append((int)(y))

plt.xlabel("Number of Cycles")
plt.ylabel("Instruction number in memory")
plt.scatter(cycles, inst_num)
plt.show()

text4 = open('data_memory.txt', 'r')
nums2 = text4.readlines()
cycles1 = []
inst_num1 = []
i = 0
for i in range(len(nums2)):
    j = 0
    while (nums2[i][j] != ' '):
        j += 1
    x = nums2[i][0:j]
    cycles1.append((int)(x))
    y = nums2[i][j:len(nums2[i]) - 1]
    inst_num1.append((int)(y))

plt.xlabel("Number of Cycles")
plt.ylabel("Instruction number in data memory (load or store)")
plt.scatter(cycles1, inst_num1)
plt.show()

index = {}
m = 0
j = 0
while m < len(inst_num):
    while j < len(inst_num) and inst_num[m] == inst_num[j]:
        j += 1
    index[inst_num[m]] = j - m
    m = j

instruc = list(index.keys())
stalls = list(index.values())
fig = plt.figure(figsize=(8, 5))
plt.bar(instruc, stalls, color='orange', width=0.4)
plt.xlabel("Instruction Number")
plt.ylabel("Number of stalls")
plt.title("Number of data Stalls")
plt.show()