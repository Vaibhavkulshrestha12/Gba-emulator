def load_rom(file_path):
    with open(file_path, 'rb') as rom_file:
        rom_data = rom_file.read()
    return bytearray(rom_data) 