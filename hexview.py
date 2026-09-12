
# Read a file in binary mode
try: 
    with open("tests/fixtures/test.txt", "rb") as file:
        byte_count = 0
        while True:
            data = file.read(16)  # Read 16 bytes at a time
            if not data:
                break
            offset = f"{byte_count:08x}"  # Format the offset as an 8-digit hexadecimal
            hex_data = ' '.join(f"{byte:02x}" for byte in data)  # Convert bytes to hex
            ascii_data = ''.join(chr(byte) if 32 <= byte <= 126 else '.' for byte in data)  # Convert bytes to ASCII
            print(f"{offset} {hex_data:<48} {ascii_data}")
            byte_count += len(data)
            print(f"Read {byte_count} bytes.")
        print(f"Total bytes read: {byte_count}")
except FileNotFoundError:
    print("Error: File not found.")
except IOError as e:
    print (f"I/O error: {e}")