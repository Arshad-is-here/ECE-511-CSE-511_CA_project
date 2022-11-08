class Decode:
    
    def __init__(self, rf):
        self.rf = rf
        self.instr_map = {
            'I': {'010':'lw'},
            'R': {
                '0000000000':'add','0100000000':'sub',
                '0000000001':'sll','00000000100':'xor',
                '0100000101':'sra','0000000110':'or',
                '0000000111':'and'
            },
            'S': {'010':'sw'},
            'SB': {'000':'beq'}
        }
        self.opcode = ''
        self.opcode_type = ''
        self.rs1 = ''
        self.rs2 = ''
        self.rd = ''
        self.offset = ''
        self.func = ''
        self.instruction = ''
        
    def storeNext(self, instruction):
        self.instruction = instruction
        
    def decode(self):
        self.opcode = self.instruction[-7:]

        if self.opcode == '0000011':
            self.opcode_type = 'I'
        elif self.opcode == '0110011':
            self.opcode_type = 'R'
        elif self.opcode == '0100011':
            self.opcode_type = 'S'
        else:
            self.opcode_type = 'SB'
        
        if self.opcode_type == 'I':
            self.func = self.instr_map['I'][self.instruction[-15:-12]]
            self.rd = int(self.instruction[-12:-7], 2)
            self.rs1 = int(self.instruction[-20:-15], 2)
            self.offset = self.instruction[-32:-20]
        elif self.opcode_type == 'R':
            self.func = self.instr_map['R'][self.instruction[-32:-25]+self.instruction[-15:-12]]
            self.rd = int(self.instruction[-12:-7], 2)
            self.rs1 = int(self.instruction[-20:-15], 2)
            self.rs2 = int(self.instruction[-25:-20], 2)
        elif self.opcode_type == 'S':
            self.func = self.instr_map['S'][self.instruction[-15:-12]]
            self.rs1 = int(self.instruction[-20:-15], 2)
            self.rs2 = int(self.instruction[-25:-20], 2)
            self.offset = self.instruction[-32:-25]+self.instruction[-12:-7]
        else:
            self.func = self.instr_map['SB'][self.instruction[-15:-12]]
            self.rs1 = int(self.instruction[-20:-15], 2)
            self.rs2 = int(self.instruction[-25:-20], 2)
            self.offset = self.instruction[-32:-25]+self.instruction[-12:-7]
        
    def decodeToExecute(self):
        return (self.opcode_type, self.func, self.rd, self.rs1, self.rs2, self.offset)



