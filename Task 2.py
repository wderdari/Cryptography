import hashlib


def avalancheCalculator(string1, string2):

    uniquebitcount = 0

    #  Convert strings to hexes
    string1_hex = hashlib.sha256(string1.encode()).hexdigest()
    string2_hex = hashlib.sha256(string2.encode()).hexdigest()

    # Converts the hexes to their corresponding binary values.
    string1_bin = bin(int(string1_hex, 16))[2:].zfill(256)  # [2:] removes the 0b
    string2_bin = bin(int(string2_hex, 16))[2:].zfill(256)  # .zfill on both variables ensures same binary length.

    # Bits of both binary values are then XOR(ed) with each other. Non-matching bits result in '1'
    xor_bits = bin(int(string1_bin, 2) ^ int(string2_bin, 2)) # XOR binary values of string 1 and 2.

    # Each non-matching bit occurence is added to the count.
    for i, bit in enumerate(xor_bits):
        if bit == "1":    # 0 = Same bits 1 = Different bits.
            uniquebitcount = uniquebitcount + 1

    return uniquebitcount




if __name__ == '__main__':
    print(avalancheCalculator("Hello World1", "Hello World2"))
