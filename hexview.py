
# Read a file in binary mode
try: 
    with open("tests/fixtures/test.txt", "rb") as file:
        byte_count = 0
        data = file.read(4)  # Read the first 4 bytes

        file_types = {
            "JPEG": b'\xff\xd8\xff', 
            "PNG": b'\x89PNG', 
            "ZIP": b'PK\x03\x04', 
            "GIF": b'GIF8', 
            "PDF": b'%PDF', 
            "ELF": b'\x7fELF', 
            "MP3": b'ID3',
            "WAV": b'RIFF',
        }

        
        detected_type = "unknown file type"
        for file_type, signature in file_types.items():
            if data.startswith(signature):
                detected_type = f"File type: {file_type}"
                break
        print(detected_type)
        file.seek(0)  # Reset file pointer to the beginning
        
        while True:
            data = file.read(16)  # Read 16 bytes at a time
            if not data:
                break
            offset = f"{byte_count:08x}"  # Format the offset as an 8-digit hexadecimal
            hex_data = ' '.join(f"{byte:02x}" for byte in data)  # Convert bytes to hex
            ascii_data = ''.join(chr(byte) if 32 <= byte <= 126 else '.' for byte in data) 
            # Convert bytes to ASCII
            print(f"{offset} {hex_data:<48} {ascii_data}")
            byte_count += len(data)
            print(f"Read {byte_count} bytes.")
        print(f"Total bytes read: {byte_count}")
except FileNotFoundError:
    print("Error: File not found.")
except IOError as e:
    print (f"I/O error: {e}")