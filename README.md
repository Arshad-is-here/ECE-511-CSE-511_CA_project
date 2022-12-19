# ECE-511-CSE-511_CA_project
  
__Functionalities added for Mid-Project Evaluation:__  
1. 5-stage pipelining (F,D,X,M,W)  
2. Instructions enabled: add, addi, sub, and, or, lw, sw, sll, sra  
  
__Work plan for final evaluation:__  
1. Handling pipeline hazards
2. Handling branches (beq)

__CA Project__ 
5-Stage Cycle accurate simulator

__Team Member Details - 
Pooja Kumari - 2019185
Shivam Jindal - 2020125
Anurag Gulati - 2020176
Arshad Iqbal - 2020180
__
In this project, we have created a 5-stage cycle accurate simulator of RISC-V CPU. 
We have used Python in this project. 

We have implemented the Simulator by creating three class which are shown below: 

CPU Class : This class is a wrapper of the entire 5-stage pipeline design. It encapsulates the instances of the fetch, decode, execute, memory, and writeback stages along with data memory, instruction memory, and register file.
Constructor of the CPU class contains the test binary, data memory latency, data memory size,instruction memory latency, instruction memory size. We have initialized the data memory, register file, memory mapped registers, fetch stages, decode stage, execute stage, memory stage, writeback stage and the test binary. Furthermore, we will initialize the program counter and branch status for branching.
Further, we initialize the instruction memory with the content of the test binary file. A simulate function is made which simulates the 5-stage pipeline and stores the CPU timeline in a log.txt file. 
We are initializing the register file with value 1 so as to make changes visible to the reader. 
Each iteration of the loop is considered as a single clock cycle. The first step in every cycle is to transfer the instructions from their previous stage to the next stage. This is followed by processing the transferred results in their new stages. Finally, we write the current state of the pipeline in log.txt. Then we pass on to the next stages, from fetch→ decode, decode → execute, execute→ memory, memory→write. Stall logic is done and if branch is taken then we update the PC to the target instruction and reset branch status in CPU. Then the logic for pipelining is done. 
At the end of each clock cycle, we are dumping the Register File and Memory mapped register. 

Data Memory class :  This class represents the data memory unit in the pipeline. Constructor is made which will instantiate the data memory and access latency and size. Read_data function is made which will read and return the data from a given memory location. Write_data functions write the data to a given memory location. And dumps the entire data memory. 

Instruction Memory class : This class represents the instruction memory unit in the pipeline. It simulates the data memory elements. The instruction memory class takes input ‘x’ and delays the CPU request by x cycles. Constructor to instantiate instruction memory and read/write latency of instruction memory. 
Read_instr performs read operation at a given address and dumps the instruction memory to get printed. 

Fetch Class: Fetch class is made which describes the class attributes and functionalities of Fetch Stage. Fetches the instruction at a given program counter value and initializes the instruction, the local instruction memory object. This class transfers the data from the Fetch stage back to the CPU, and further passes to the Decode stage. 

Decode Class: Decode class describes the class attributes and functionalities of the Decode stage. We are mapping the opcode to the class of instruction, initializing the opcode, the class of opcode, source register 1, register 2, destination register and offset, instruction function, instruction and track the status of stall for Decode. Decode function performs the decoding of a binary instruction.  We further return the decoded segments from decode stage back to the CPU for transferring to the execute stage.

Execute Class: This class describes the class attributes and functionalities of the execute stage. Initializing the local register file, opcode type, function of the instruction, source reg1, reg2, offset, destination reg, value destinations, local program counter, instruction, and branch status. The Execute_compute function will execute the instruction received from the Decode stage and transfer the parameters from the execute stage back to CPU and further passed on to the Memory stage. 

Memory Class : This class describes the  class attributes and functionalities of the memory stage. Constructor to instantiate an object of the memory stage by initializing the local register file object, local data memory object, the functionality of instruction, src red1, src reg2, instruction offset, destination register, value of destination, local program counter. Memory_compute performs the memory operations and memory_to_writeback transfers the parameters from Memory stage back to the CPU and further sent to the Writeback stage.

Writeback Class: This  class describes the  class attributes and functionalities of the writeback stage. Gives back the updated register file to the CPU.

How to use the code and graph plotter: 
In testbinary.txt, we have given our instruction in the assembly language which will be passed to the assembly.py. Now, assembly,py will convert these instructions into binary code, and will write the binary code in testfile.txt. This testfile.txt is finally passed to the cpu.py and now we just need to run cpu.py which will create the log file and plot all the required graphs.
