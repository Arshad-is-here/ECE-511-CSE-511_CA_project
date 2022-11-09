class Decode:

    def __init__(self):
        self.opcode_map = {'0010011': 'I', '0110011': 'R', '0100011': 'S', '1100011': 'SB', '0000011' : 'L'}
        self.instr_map = {
            'I': {'000': 'addi'},
            'R': {
                '0000000000': 'add', '0100000000': 'sub',
                '0000000001': 'sll', '0100000101': 'sra',
                '0000000110': 'or', '0000000111': 'and'
            },
            'S': {'010': 'sw'},
            'SB': {'000': 'beq'},
            'L': {'010': 'lw'}
        }
        self.opcode = ''
        self.opcode_type = ''
        self.rs1 = ''
        self.rs2 = ''
        self.rd = ''
        self.offset = ''
        self.func = ''
        self.instruction = ''

    def decode(self, instruction):
        self.instruction = instruction
        if self.instruction != '':
            self.opcode = self.instruction[-8:-1]

            self.opcode_type = self.opcode_map[self.opcode]

            if self.opcode_type == 'I':
                self.func = self.instr_map['I'][self.instruction[-15 - 1:-12 - 1]]
                self.rd = int(self.instruction[-12 - 1:-7 - 1], 2)
                self.rs1 = int(self.instruction[-20 - 1:-15 - 1], 2)
                self.offset = self.instruction[-32 - 1:-20 - 1]
            elif self.opcode_type == 'L':
                self.func = self.instr_map['L'][self.instruction[-15 - 1:-12 - 1]]
                self.rd = int(self.instruction[-12 - 1:-7 - 1], 2)
                self.rs1 = int(self.instruction[-20 - 1:-15 - 1], 2)
                self.offset = self.instruction[-32 - 1:-20 - 1]
            elif self.opcode_type == 'R':
                self.func = self.instr_map['R'][self.instruction[-32 - 1:-25 - 1] + self.instruction[-15 - 1:-12 - 1]]
                self.rd = int(self.instruction[-12 - 1:-7 - 1], 2)
                self.rs1 = int(self.instruction[-20 - 1:-15 - 1], 2)
                self.rs2 = int(self.instruction[-25 - 1:-20 - 1], 2)
            elif self.opcode_type == 'S':
                self.func = self.instr_map['S'][self.instruction[-15 - 1:-12 - 1]]
                self.rs1 = int(self.instruction[-20 - 1:-15 - 1], 2)
                self.rs2 = int(self.instruction[-25 - 1:-20 - 1], 2)
                self.offset = self.instruction[-32 - 1:-25 - 1] + self.instruction[-12 - 1:-7 - 1]
            else:
                self.func = self.instr_map['SB'][self.instruction[-15 - 1:-12 - 1]]
                self.rs1 = int(self.instruction[-20 - 1:-15 - 1], 2)
                self.rs2 = int(self.instruction[-25 - 1:-20 - 1], 2)
                self.offset = self.instruction[-32 - 1:-25 - 1] + self.instruction[-12 - 1:-7 - 1]

    def decodeToExecute(self):
        return (self.opcode_type, self.func, self.rd, self.rs1, self.rs2, self.offset, self.instruction)