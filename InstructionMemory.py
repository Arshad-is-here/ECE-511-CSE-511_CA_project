class InstructionMemory:
    
    def __init__(self, access_delay=1, size=512):
        self.access_delay = access_delay
        self.size = size
        self.mem = ['' for _ in range(size)]
    
    def initialize(self, filepath):
        instr = open(filepath, 'r')
        self.mem = instr.readlines()
    
    def read_instr(self, addr):
        return self.mem[addr]
    
    def dump(self):
        return self.mem
        