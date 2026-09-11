
# Read a file in binary mode
try: 
    with open("tests/fixtures/test.txt", "rb") as file:
        byte_count = 0
        while True:
            data = file.read(16)  # Read 16 bytes at a time
            if not data:
                break
            byte_count += len(data)
            print(f"Read {byte_count} bytes.")
        print(f"Total bytes read: {byte_count}")
except FileNotFoundError:
    print("Error: File not found.")
except IOError as e:
    print (f"I/O error: {e}")