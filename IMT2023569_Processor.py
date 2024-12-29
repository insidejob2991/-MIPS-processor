def binary_to_decimal(binary):
    decimal = 0
    binary_str = str(binary)  # Convert to string to handle individual digits

    for i in range(len(binary_str)):
        
        digit =int(binary_str[i])
        power = len(binary_str) - 1 - i
        decimal += digit * (2 ** power)

    return decimal

def bin_to_int_signed(binary):
    if binary[0] == '1':
        sign = -1
    else:
        sign = 1
    magnitude = int(binary[1:], 2)
    return sign * magnitude
        



def binary_to_int(binary_str):
    # Convert binary string to integer
    return int(binary_str, 2)
class MIPSProcessor:
    def __init__(self):
        # Initialize components
        self.registers = [0] * 32  # 32 general-purpose registers
        self.pc = 0  # Program Counter
        self.memory = [0] * 1024  # Memory
        self.ins_memory=[0] * 25
        self.halt_flag = False  # Flag to indicate HALT instruction
        self.branch_flag = False  # Flag to indicate branch
        self.jump_flag = False  # Flag to indicate jump
        self.branch_target = 0  # Target address for branch
        self.jump_target = 0  # Target address for jump



    def executeR(self, opcode, rs, rt, rd,shamt,funct):
        #print("R type instruction executed")
        # Execute instruction
        func=binary_to_decimal(funct)
        if binary_to_decimal(opcode) == 0:  # R-type
            #print(binary_to_decimal(funct))
            
            
            if binary_to_decimal(funct) == 32:  # ADD
                self.registers[binary_to_decimal(rd)] = self.registers[binary_to_decimal(rs)] + self.registers[binary_to_decimal(rt)]
                #print(self.registers[binary_to_decimal(rd)])
                self.pc+=4
            elif binary_to_decimal(funct) == 36:  # AND
                self.registers[rd] = self.registers[rs] & self.registers[rt]
                self.pc+=4
            elif binary_to_decimal(funct) == 0:  # NOP
                self.pc+=4
                pass
            elif binary_to_decimal(funct) == 34:  # sub
                #print("sub executed")
                self.memory[binary_to_decimal(rd)]=self.memory[binary_to_decimal(rt)]-self.memory[binary_to_decimal(rs)]
                self.pc+=4
            elif binary_to_decimal(funct)==12: #continue
               # print("syscall")
                if self.registers[2]==5:
                    n = int(input())
                    self.registers[2] = n
                elif self.registers[2]==1:
                    print("answer",self.registers[4])#a0
                elif self.registers[2]==10:
                    exit()
                self.pc+=4
                
                

    def executeI(self,opcode,rs,rt,imm):
        #print("i type instruction executed")    
        if binary_to_decimal(opcode)==15: #load upper imediate
            tar=imm+"0000"*4
            m=268500992
            #tar=int((binary_to_decimal(tar)%m)/4)
            #print(binary_to_decimal(tar))
           
            self.registers[binary_to_decimal(rt)]=binary_to_decimal(tar)
            self.pc+=4
        elif binary_to_decimal(opcode)==9: #load immediate
           # print("addiu")
            self.registers[binary_to_decimal(rt)]= self.registers[binary_to_decimal(rs)]+ binary_to_decimal(imm)
            self.pc+=4
        elif binary_to_decimal(opcode)==43: #store
            #print(self.registers[binary_to_decimal(rs)],"[]")
            m=268500992
            self.memory[int(((self.registers[binary_to_decimal(rs)]+bin_to_int_signed(imm))%m)/4)]=self.registers[binary_to_decimal(rt)]
            #print(f"rt={binary_to_decimal(rt)},rs={binary_to_decimal(rs)},imm={bin_to_int_signed(imm)} ")
            self.pc+=4
        elif binary_to_decimal(opcode)==35: #load
            m=268500992
            self.registers[binary_to_decimal(rt)]=self.memory[int(((self.registers[binary_to_decimal(rs)]+bin_to_int_signed(imm))%m)/4)]
            #print(f"rt={binary_to_decimal(rt)},rs={binary_to_decimal(rs)},imm={bin_to_int_signed(imm)} ")
            #print(binary_to_decimal(rs),bin_to_int_signed(imm))
            #print(self.registers[binary_to_decimal(rt)],"!!!")
            self.pc+=4
        elif binary_to_decimal(opcode)==4: #beq
            if self.registers[binary_to_decimal(rt)]!=self.registers[binary_to_decimal(rs)]:
                self.pc+=4
            else:
                self.pc+=bin_to_int_signed(imm)*4 + 4


        elif binary_to_decimal(opcode) == 8:  # ADDI
            self.registers[binary_to_decimal(rt)] = self.registers[binary_to_decimal(rs)] + bin_to_int_signed(imm)
            self.pc+=4

        elif binary_to_decimal(opcode) == 12:  # ANDI
            self.registers[rt] = self.registers[rs] & imm
            self.pc+=4


    def memory_access(self):
        # Memory access stage (not implemented in this example)
        pass

    def write_back(self):
        # Write back stage (not implemented in this example)
        pass

    def run(self):
        while not self.halt_flag:
            instruction = self.fetch()
            opcode, rs, rt, rd, immediate = self.decode(instruction)
            self.execute(opcode, rs, rt, rd, immediate)
            if self.branch_flag:
                self.pc = self.branch_target
                self.branch_flag = False
            elif self.jump_flag:
                self.pc = self.jump_target
                self.jump_flag = False
    def executeJ(self,adre):
        #print("j executed")
        target = adre + "00"
        target = binary_to_decimal(target)
        self.pc = target

# Example program to compute factorial of 5
#factorial_program = [
   # 0x20020005,  # ADDI $2, $0, 5 (initialize $2 to 5)
    #0x00000003,  # HALT
#]
y = MIPSProcessor()
f = open("IMT2023128_machine.txt","r")
memory  = f.readlines()
for i in range(1024):
    y.memory[i] = binary_to_int(memory[i])
m = 4194304   #variable store for pc
y.pc=4194304
#(pc%m)/4
z=open("IMT2023128_fdh.txt","r")
for j in z:
    x1=int((y.pc%m)/4)
    y.ins_memory[x1]=j[0:32]
    y.pc+=4
y.pc=4194304
y.registers[2]=0
c = 0
while(True):
    x1=int((y.pc%m)/4)
    #print(binary_to_decimal(y.ins_memory[x1][0:6]),c)
    #print(type(y.ins_memory[x1][0:6]))
    c+=1
    #print(x1)
    z3=y.ins_memory[x1]
    #print(type(z3))
   # print(z3)
    #print("!",y.registers[2])
    z2=binary_to_decimal(z3[0:6])
    if z2 !=0 and z2!=2:
        y.executeI((y.ins_memory[x1])[0:6],(y.ins_memory[x1])[6:11],(y.ins_memory[x1])[11:16],(y.ins_memory[x1])[16:])
    elif z2==0:
        y.executeR((y.ins_memory[x1])[0:6],(y.ins_memory[x1])[6:11],(y.ins_memory[x1])[11:16],(y.ins_memory[x1])[16:21],(y.ins_memory[x1])[21:26],(y.ins_memory[x1])[26:])
    elif z2==2:
        y.executeJ(y.ins_memory[x1][6:])
    

    #print(y.memory[0:17])
    #print(y.registers[0:17])
        
        #r type instructio
    



#processor.memory[:len(factorial_program)] = factorial_program
#processor.run()
#2685 -> 0
#2685+4 -> 1
#8 -> 2

#x%2685)/4