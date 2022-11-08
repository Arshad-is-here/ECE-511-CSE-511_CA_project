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
    
    def getNext():
        pass

    def decode(self, instruction):
        opcode = instruction[-7:]
        opcode_type = ''
        rs1 = ''
        rs2 = ''
        rd = ''
        offset = ''
        func = ''

        if opcode == '0000011':
            opcode_type = 'I'
        elif opcode == '0110011':
            opcode_type = 'R'
        elif opcode == '0100011':
            opcode_type = 'S'
        else:
            opcode_type = 'SB'
        
        if opcode_type == 'I':
            func = self.instr_map['I'][instruction[-15:-12]]
            rd = int(instruction[-12:-7], 2)
            rs1 = int(instruction[-20:-15], 2)
            offset = instruction[-32:-20]
        elif opcode_type == 'R':
            func = self.instr_map['R'][instruction[-32:-25]+instruction[-15:-12]]
            rd = int(instruction[-12:-7], 2)
            rs1 = int(instruction[-20:-15], 2)
            rs2 = int(instruction[-25:-20], 2)
        elif opcode_type == 'S':
            func = self.instr_map['S'][instruction[-15:-12]]
            rs1 = int(instruction[-20:-15], 2)
            rs2 = int(instruction[-25:-20], 2)
            offset = instruction[-32:-25]+instruction[-12:-7]
        else:
            func = self.instr_map['SB'][instruction[-15:-12]]
            rs1 = int(instruction[-20:-15], 2)
            rs2 = int(instruction[-25:-20], 2)
            offset = instruction[-32:-25]+instruction[-12:-7]
        
        return (opcode_type, func, rd, rs1, rs2, offset)



