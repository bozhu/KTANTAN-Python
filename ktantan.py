#!/usr/bin/env python


IR = (
    1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 
    0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 
    1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 
    0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 
    0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 
    1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 
    0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 
    1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 
    0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 
    1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 
    1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 
    0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 
    1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 
    0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 
    0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 
    1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,
)

k_a_index = (
    63,  31,  31,  15,  14,  60,  40,  49,  35,  54,  45,  58,  37,  74,  69,  74, 
    53,  43,  71,  63,  30,  45,  11,  54,  28,  41,   3,  38,  60,  25,  34,   5, 
    26,  20,   9,   2,  20,  24,   1,   2,  52,  24,  17,   3,   6,  76,  72,  49, 
    19,  23,  15,  14,  12,  24,  16,   1,   2,   4,  40,  48,  17,  18,   5,  10, 
     4,   8,  64,  64,  65,  51,  23,  47,  15,  78,  76,  73,  67,  55,  47,  63, 
    47,  62,  29,  26,   5,  10,  36,  56,  33,  50,  21,  42,   5,  58,  20,  25, 
     3,   6,  12,  56,  16,  33,   3,  70,  60,  41,  67,  71,  78,  77,  59,  39, 
    79,  79,  62,  45,  59,  23,  46,  13,  42,  52,  41,  66,  53,  42,  53,  27, 
    38,  13,  74,  52,  25,  35,   7,  62,  44,  73,  51,  22,  29,  11,   6,  44, 
    72,  65,  50,  37,  75,  55,  46,  77,  75,  70,  61,  27,  39,  15,  46,  76, 
    57,  34,  69,  59,  38,  61,  43,  70,  77,  58,  21,  43,   7,  30,  44,   9, 
    18,  36,   9,  50,  36,  57,  19,  22,  13,  10,  68,  56,  17,  19,   7,  14, 
    28,  40,   1,  66,  68,  57,  35,  55,  31,  30,  13,  10,   4,  72,  48,  33, 
    51,  39,  78,  61,  26,  21,  11,   6,  12,   8,  32,  64,  49,  18,  37,  11, 
    22,  28,   9,   2,   4,   8,   0,  48,  32,  65,  67,  54,  29,  27,   7,  14, 
    12,   8,   0,   0,  16,  32,   1,  34,  68,  73,  66,  69,  75,  71,
)

k_b_index = (
    31,  63,  63,  47,  14,  76,  40,  17,  67,  22,  77,  26,  69,  10,  69,  10, 
    21,  43,   7,  79,  62,  45,  11,  70,  60,  41,  19,  70,  28,  73,  34,  21, 
    74,  52,  41,  18,  68,  56,  33,   2,  68,  56,  49,  35,   6,  76,   8,  17, 
    51,  55,  63,  46,  28,  72,  48,  49,  34,  20,  72,  16,  65,  50,  53,  58, 
    36,   8,  64,   0,   1,  19,  55,  47,  15,  78,  12,   9,   3,  23,  47,  31, 
    79,  30,  77,  58,  37,  26,  68,  24,  65,  18,  69,  42,   5,  74,  52,  57, 
    51,  38,  12,  72,  48,  33,   3,  70,  28,  41,   3,  71,  14,  13,  27,  39, 
    15,  79,  30,  45,  27,  71,  46,  29,  74,  20,  73,   2,  69,  42,  21,  75, 
    38,  13,  74,  20,  57,  35,   7,  78,  44,   9,  67,  54,  61,  43,  22,  76, 
     8,  65,  18,  37,  11,  71,  46,  13,  75,   6,  29,  59,  39,  31,  78,  12, 
    73,  34,   5,  75,  38,  29,  75,   6,  77,  26,  53,  43,  23,  78,  44,  25, 
    66,  36,   9,  66,  36,  25,  67,  54,  45,  10,  68,  24,  49,  51,  39,  30, 
    76,  40,   1,  66,   4,  25,  35,  23,  79,  62,  61,  42,   4,  72,  16,  33, 
    19,  71,  14,  77,  58,  53,  59,  54,  44,  24,  64,   0,  65,  50,  37,  27, 
    70,  60,  57,  50,  52,  40,   0,  64,  32,   1,  67,  22,  61,  59,  55,  62, 
    60,  56,  32,  16,  64,  32,  17,  66,   4,  73,   2,   5,  11,   7,
)


def num2bits(num, bitlength):
    bits = []
    for i in range(bitlength):
        bits.append(num & 1)
        num >>= 1
    return bits

def bits2num(bits):
    num = 0
    for i, x in enumerate(bits):
        assert x == 0 or x == 1
        num += (x << i)
    return num


class KTANTAN():
    def __init__(self, master_key = 0, version = 32):
        assert version in (32, 48, 64)
        self.version = version

        if 32 == self.version:
            self.LEN_L1 = 13
            self.LEN_L2 = 19
            self.X = (None, 12, 7, 8, 5, 3) # starting from 1
            self.Y = (None, 18, 7, 12, 10, 8, 3)
        elif 48 == self.version:
            self.LEN_L1 = 19
            self.LEN_L2 = 29
            self.X = (None, 18, 12, 15, 7, 6)
            self.Y = (None, 28, 19, 21, 13, 15, 6)
        else:
            self.LEN_L1 = 25
            self.LEN_L2 = 39
            self.X = (None, 24, 15, 20, 11, 9)
            self.Y = (None, 38, 25, 33, 21, 14, 9)

        self.change_key(master_key)


    def change_key(self, master_key):
        self.key = tuple(num2bits(master_key, 80))


    def one_round_enc(self, round):
        self.f_a = self.L1[self.X[1]] ^ self.L1[self.X[2]]  \
                ^ (self.L1[self.X[3]] & self.L1[self.X[4]]) \
                ^ (self.L1[self.X[5]] & IR[round])          \
                ^ self.key[k_a_index[round]]

        self.f_b = self.L2[self.Y[1]] ^ self.L2[self.Y[2]]  \
                ^ (self.L2[self.Y[3]] & self.L2[self.Y[4]]) \
                ^ (self.L2[self.Y[5]] & self.L2[self.Y[6]]) \
                ^ self.key[k_b_index[round]]

        self.L1.pop()
        self.L1.insert(0, self.f_b)

        self.L2.pop()
        self.L2.insert(0, self.f_a)


    def enc(self, plaintext, from_round = 0, to_round = 253):
        self.plaintext_bits = num2bits(plaintext, self.version)
        self.L2 = self.plaintext_bits[:self.LEN_L2]
        self.L1 = self.plaintext_bits[self.LEN_L2:]

        for round in range(from_round, to_round + 1):
            self.one_round_enc(round)
            if self.version > 32:
                self.one_round_enc(round)
                if self.version > 48:
                    self.one_round_enc(round)
        return bits2num(self.L2 + self.L1)


    def one_round_dec(self, round):
        self.f_a = self.L2[0] ^ self.L1[self.X[2] + 1]              \
                ^ (self.L1[self.X[3] + 1] & self.L1[self.X[4] + 1]) \
                ^ (self.L1[self.X[5] + 1] & IR[round])              \
                ^ self.key[k_a_index[round]]

        self.f_b = self.L1[0] ^ self.L2[self.Y[2] + 1]              \
                ^ (self.L2[self.Y[3] + 1] & self.L2[self.Y[4] + 1]) \
                ^ (self.L2[self.Y[5] + 1] & self.L2[self.Y[6] + 1]) \
                ^ self.key[k_b_index[round]]

        self.L1.pop(0)
        self.L1.append(self.f_a)

        self.L2.pop(0)
        self.L2.append(self.f_b)


    def dec(self, ciphertext, from_round = 253, to_round = 0):
        self.ciphertext_bits = num2bits(ciphertext, self.version)
        self.L2 = self.ciphertext_bits[:self.LEN_L2]
        self.L1 = self.ciphertext_bits[self.LEN_L2:]

        for round in range(from_round, to_round - 1, -1):
            self.one_round_dec(round)
            if self.version > 32:
                self.one_round_dec(round)
                if self.version > 48:
                    self.one_round_dec(round)
        return bits2num(self.L2 + self.L1)



if __name__ == '__main__':
    key = 0xFFFFFFFFFFFFFFFFFFFF
    plaintext = 0x00000000

    myKTANTAN = KTANTAN(key)

    print 'key =', hex(key)
    print 'plain =', hex(plaintext)

    encrypted = myKTANTAN.enc(plaintext)
    print 'encrypted =', hex(encrypted)
    decrypted = myKTANTAN.dec(encrypted)
    print 'decrypted =', hex(decrypted)
    
