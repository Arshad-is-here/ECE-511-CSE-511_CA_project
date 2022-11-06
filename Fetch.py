from InstructionMemory import InstructionMemory

class Fetch:
    
    def __init__(self, imem):
        self.instruction = ''
        self.imem = imem

    def fetch(self, PC):
        return self.imem.read_instr(PC)

