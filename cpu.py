class CPU:
    def __init__(self):
        self.a = 0   
        self.f = 0    
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.h = 0
        self.l = 0

        
        self.pc = 0x100  
        self.sp = 0xFFFE 

        
        self.zero_flag = False
        self.subtract_flag = False
        self.half_carry_flag = False
        self.carry_flag = False

    def reset(self):
        self.pc = 0x100  
        self.sp = 0xFFFE 
      
        self.a = 0
        self.f = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.h = 0
        self.l = 0
        self.zero_flag = False
        self.subtract_flag = False
        self.half_carry_flag = False
        self.carry_flag = False

    def fetch(self, memory):
        opcode = memory[self.pc]
        self.pc += 1
        return opcode

    def execute(self, opcode, memory):  
        if opcode == 0x00: 
            pass 
        elif opcode == 0xC3:  
            low_byte = memory[self.pc]
            high_byte = memory[self.pc + 1]
            self.pc = (high_byte << 8) | low_byte
        else:
            print(f"Unimplemented opcode: {hex(opcode)}")

    def step(self, memory):
        opcode = self.fetch(memory)
        self.execute(opcode, memory)  
