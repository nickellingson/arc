x = 4
print(type(bin(x)))
print(x, bin(x), hex(x))
print(type(format(x, "b")))
print(format(x, "b"))
print()

x = 10
print(x, bin(x))

x = 15
print(x, bin(x))

x = 30
print(x, bin(x))

x = 255
# 1111 1111 (binary)
# 2 ^ 7
# 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128
# 255 (decimal)
# 0xff (hex)

# Rightmost bit → 2^0 = 1
# Next bit → 2^1 = 2
# ...

# Binary left to right (most significat bit on the left) MSB
# Compute right to left (least signicant bit) LSB

# Endianess deals with byte order
# 32 bit integer = 4 bytes
# 64 bit integer = 8 bytes

# little endian
# addr:   1000   1001   1002   1003
# value:  0x78   0x56   0x34   0x12

# little-endian vs big-endian, for a single byte, there’s no difference
print(x, bin(x), hex(x))
print()

# arm = little endian
# little endian = least significant byte first
x = 10000
print(x, bin(x), hex(x))

print("big", x.to_bytes(4, "big"))
print("little", x.to_bytes(4, "little"))

import sys
print("arm endian", sys.byteorder)

# 0x12 = 00010010
# 0x34 = 00110100

# 0x1234 = 00010010 00110100

# little endian
# address ->
# 00   01
# 0x34 0x12

# big endian
# address ->
# 00   01
# 0x12 0x34