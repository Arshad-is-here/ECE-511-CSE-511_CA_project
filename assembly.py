opcode = {"add": "01100",
          "sub": "01100",
          "and": "01100",
          "or": "01100",
          "addi": "00100",
          "beq": "11000",
          "lw": "00000",
          "sw": "01000",
          "sll": "01100",
          "sra": "01100"}

registers = {"R0": "00000",
             "R1": "00001",
             "R2": "00010",
             "R3": "00011",
             "R4": "00100",
             "R5": "00101",
             "R6": "00110",
             "R7": "00111",
             "R8": "01000",
             "R9": "01001",
             "R10": "01010",
             "R11": "01011",
             "R12": "01100",
             "R13": "01101",
             "R14": "01110",
             "R15": "01111",
             "R16": "10000",
             "R17": "10001",
             "R18": "10010",
             "R19": "10011",
             "R20": "10100",
             "R21": "10101",
             "R22": "10110",
             "R23": "10111",
             "R24": "11000",
             "R25": "11001",
             "R26": "11010",
             "R27": "11011",
             "R28": "11100",
             "R29": "11101",
             "R30": "11110",
             "R31": "11111"}

labels = {}

def encode(instructions):
    inst = instructions[0]
    if inst == "add":
        return "00000" + "00" + registers[instructions[3]] + registers[instructions[2]] + "000" + registers[
            instructions[1]] + opcode[inst] + "11"
    elif inst == "sub":
        return "01000" + "00" + registers[instructions[3]] + registers[instructions[2]] + "000" + registers[
            instructions[1]] + opcode[inst] + "11"
    elif inst == "and":
        return "00000" + "00" + registers[instructions[3]] + registers[instructions[2]] + "111" + registers[
            instructions[1]] + opcode[inst] + "11"
    elif inst == "or":
        return "00000" + "00" + registers[instructions[3]] + registers[instructions[2]] + "110" + registers[
            instructions[1]] + opcode[inst] + "11"
    elif inst == "addi":
        return format(int(instructions[3]), '012b') + registers[instructions[2]] + "000" + registers[instructions[1]] + \
               opcode[inst] + "11"
    elif inst == "beq":
        offset = instructions[3]
        offset = labels[offset]
        offset = format(offset, '012b')
        return offset[0] + offset[2:8] + registers[instructions[2]] + registers[instructions[1]] + "000" + offset[8:] + \
               offset[1] + opcode[inst] + "11"
    elif inst == "lw":
        offset = instructions[2].split("(")[0]
        offset = format(int(offset), '012b')
        r1 = instructions[2].split("(")[1].replace(")", "")
        return offset + registers[r1] + "010" + registers[instructions[1]] + opcode[inst] + "11"
    elif inst == "sw":
        offset = instructions[2].split("(")[0]
        offset = format(int(offset), '012b')
        r1 = instructions[2].split("(")[1].replace(")", "")
        return offset[:7] + registers[instructions[1]] + registers[r1] + "010" + offset[7:] + opcode[inst] + "11"
    elif inst == "sll":
        return "00000" + "00" + registers[instructions[3]] + registers[instructions[2]] + "001" + registers[
            instructions[1]] + opcode[inst] + "11"
    elif inst == "sra":
        return "01000" + "00" + registers[instructions[3]] + registers[instructions[2]] + "101" + registers[
            instructions[1]] + opcode[inst] + "11"


def main():
    instructions = []
    with open('testbinary.txt') as f:
        for inst in f:
            if not inst.isspace():
                line = inst.replace("\n", "")
                instructions.append(line)

    keys = opcode.keys()
    line_number = 0
    for instr in instructions:
        word = instr.split()[0]
        if word not in keys:
            labels[word[:-1]] = line_number
        line_number += 1

    binary = []
    pc = 0
    while pc < len(instructions):
        instr = instructions[pc]
        if pc in labels.values():
            lists = instr.split()[1:]
            binary.append(encode(lists))
        else:
            binary.append(encode(instr.split()))
        pc += 1
    print(labels)
    text = open('testfile.txt', 'w')
    for element in binary:
        text.write(element + "\n")
    text.close()
    #print(labels)


if __name__ == "__main__":
    main()