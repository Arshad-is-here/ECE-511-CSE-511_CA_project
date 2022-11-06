from numpy import zeros

class DataMemory:
    
    def __init__(self, access_latency=1, size=512):
        self.access_latency = access_latency
        self.size = size
        self.mem = zeros(size)

    def read_data(self, raddr):
        return self.mem[raddr]
    
    def write_data(self, waddr, wdata):
        self.mem[waddr] = wdata
    
    def dump(self):
        return self.mem