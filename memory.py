class Memory:
    def __init__(self):
        self.memory = [0] * 65536 

    def load_rom(self, rom_data):
        if not isinstance(rom_data, (list, bytearray)):
            raise ValueError("rom_data must be a list or bytearray")

        rom_size = len(rom_data)
        
        if rom_size > len(self.memory):
            print(f"Warning: ROM size ({rom_size} bytes) exceeds memory size ({len(self.memory)} bytes). Truncating ROM data.")
        
        
        for i in range(min(rom_size, len(self.memory))):
            self.memory[i] = rom_data[i]

    def __getitem__(self, address):
        return self.memory[address]

    def __setitem__(self, address, value):
        self.memory[address] = value
