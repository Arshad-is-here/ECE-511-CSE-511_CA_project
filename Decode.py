class Decode:

    """
    @brief      Describes the class attributes and functionalities of the Decode stage.
    """

    def __init__(self):

        """
        @brief      Constructor to create the object of decode stage
        @param      None
        @return     None
        """

        self.opcode_map = {                                             # mapping opcode to the class of instruction
                '0010011': 'I', '0110011': 'R', '0100011': 'S', 
                '1100011': 'SB', '0000011' : 'L'
            }
        self.instr_map = {                                              # mapping the exact instruction using other info
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
        self.opcode = ''                    # initializing opcode
        self.opcode_type = ''               # initializing the class of opcode
        self.rs1 = ''                       # initializing source register 1
        self.rs2 = ''                       # initializing source register 2
        self.rd = ''                        # initializing destination register
        self.offset = ''                    # initializing offset 
        self.func = ''                      # initializing intruction function
        self.instruction = ''               # inititalizing instruction

    def decode(self, instruction):

        """
        @brief      Performs he decoding of a binary instruction
        @param      instruction: the instruction to be decoded
        @return     None
        """

        self.instruction = instruction  
        if self.instruction != '':                              # if the instruction is not empty, we have to decode it
            self.opcode = self.instruction[-8:-1]               # extracting opcode out of the instruction

            self.opcode_type = self.opcode_map[self.opcode]     # decoding the type of opcode from the mapping

            if self.opcode_type == 'I':                         # if the instruction is of immediate (I) type
                self.func = self.instr_map['I'][self.instruction[-15 - 1:-12 - 1]]
                self.rd = int(self.instruction[-12 - 1:-7 - 1], 2)
                self.rs1 = int(self.instruction[-20 - 1:-15 - 1], 2)
                self.offset = self.instruction[-32 - 1:-20 - 1]

            elif self.opcode_type == 'L':                       # if the instruction is of load (L) type
                self.func = self.instr_map['L'][self.instruction[-15 - 1:-12 - 1]]
                self.rd = int(self.instruction[-12 - 1:-7 - 1], 2)
                self.rs1 = int(self.instruction[-20 - 1:-15 - 1], 2)
                self.offset = self.instruction[-32 - 1:-20 - 1]

            elif self.opcode_type == 'R':                       # if the instruction is of register (R) type
                self.func = self.instr_map['R'][self.instruction[-32 - 1:-25 - 1] + self.instruction[-15 - 1:-12 - 1]]
                self.rd = int(self.instruction[-12 - 1:-7 - 1], 2)
                self.rs1 = int(self.instruction[-20 - 1:-15 - 1], 2)
                self.rs2 = int(self.instruction[-25 - 1:-20 - 1], 2)

            elif self.opcode_type == 'S':                       # if the instruction is of store (S) type
                self.func = self.instr_map['S'][self.instruction[-15 - 1:-12 - 1]]
                self.rs1 = int(self.instruction[-20 - 1:-15 - 1], 2)
                self.rs2 = int(self.instruction[-25 - 1:-20 - 1], 2)
                self.offset = self.instruction[-32 - 1:-25 - 1] + self.instruction[-12 - 1:-7 - 1]

            else:                                               # if the instruction is of SB type
                self.func = self.instr_map['SB'][self.instruction[-15 - 1:-12 - 1]]
                self.rs1 = int(self.instruction[-20 - 1:-15 - 1], 2)
                self.rs2 = int(self.instruction[-25 - 1:-20 - 1], 2)
                self.offset = self.instruction[0] + self.instruction[24] + self.instruction[1:7] + self.instruction[20:24]

    def decodeToExecute(self):

        """
        @brief      Returns the decoded segments from decode stage back to the 
                    CPU for transfering to the execute stage.
        @param      None
        @Returns    tuple containing the relevant information regarding the instruction
        """

        return [self.opcode_type, self.func, self.rd, self.rs1, self.rs2, self.offset, self.instruction]