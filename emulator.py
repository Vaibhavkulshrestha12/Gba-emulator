import os
from cpu import CPU
from memory import Memory
from rom_loader import load_rom

def main(rom_path):
    
    if not os.path.isfile(rom_path):  
        print(f"Error: The file '{rom_path}' does not exist.")
        return  

    cpu = CPU()
    memory = Memory()

   
    rom_data = load_rom(rom_path)
    
   
    print(f"Loaded ROM data type: {type(rom_data)}")  

    if not isinstance(rom_data, (list, bytearray)):
        raise ValueError("rom_data must be a list or bytearray")

    memory.load_rom(rom_data)

   
    while True:
        cpu.step(memory)

if __name__ == "__main__":
    rom_path = r"C:\Users\vaibhav kulshrestha\desktop\gbc-emulator\rom files\Pokemon Red (U) [S][BF].gb"  
    main(rom_path)
