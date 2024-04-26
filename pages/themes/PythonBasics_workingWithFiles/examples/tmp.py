# Open the file in binary mode
with open('./test_file.txt', 'rb') as file:
    # Read the file line by line
    for line in file:
        # Convert each byte of the line to its binary representation
        binary_line = ' '.join(f'{byte:08b}' for byte in line)
        print(binary_line)
