#!/usr/bin/env python

# ktantan-32
LEN_L_1 = 13
LEN_L_2 = 19
X = (None, 12, 7, 8, 5, 3) # starting from 1
Y = (None, 18, 7, 12, 10, 8, 3)

# ktantan-48
#LEN_L_1 = 19
#LEN_L_2 = 29
#X = (None, 18, 12, 15, 7, 6)
#Y = (None, 28, 19, 21, 13, 15, 6)

# ktantan-64
#LEN_L_1 = 25
#LEN_L_2 = 39
#X = (None, 24, 15, 20, 11, 9)
#Y = (None, 38, 25, 33, 21, 14, 9)


IR = (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 
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
      1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,)

k_a = (63,  31,  31,  15,  14,  60,  40,  49,  35,  54,  45,  58,  37,  74,  69,  74, 
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
       12,   8,   0,   0,  16,  32,   1,  34,  68,  73,  66,  69,  75,  71,)

k_b = (47,  15,  15,  31,  62,  76,  24,  33,  67,  38,  77,  42,  69,  58,  69,  58, 
       37,  27,  55,  79,  14,  29,  59,  70,  12,  25,  35,  70,  44,  73,  18,  37, 
       74,   4,  25,  34,  68,   8,  17,  50,  68,   8,   1,  19,  54,  76,  56,  33, 
        3,   7,  15,  30,  44,  72,   0,   1,  18,  36,  72,  32,  65,   2,   5,  10, 
       20,  56,  64,  48,  49,  35,   7,  31,  63,  78,  60,  57,  51,  39,  31,  47, 
       79,  46,  77,  10,  21,  42,  68,  40,  65,  34,  69,  26,  53,  74,   4,   9, 
        3,  22,  60,  72,   0,  17,  51,  70,  44,  25,  51,  71,  62,  61,  43,  23, 
       63,  79,  46,  29,  43,  71,  30,  45,  74,  36,  73,  50,  69,  26,  37,  75, 
       22,  61,  74,  36,   9,  19,  55,  78,  28,  57,  67,   6,  13,  27,  38,  76, 
       56,  65,  34,  21,  59,  71,  30,  61,  75,  54,  45,  11,  23,  47,  78,  60, 
       73,  18,  53,  75,  22,  45,  75,  54,  77,  42,   5,  27,  39,  78,  28,  41, 
       66,  20,  57,  66,  20,  41,  67,   6,  29,  58,  68,  40,   1,   3,  23,  46, 
       76,  24,  49,  66,  52,  41,  19,  39,  79,  14,  13,  26,  52,  72,  32,  17, 
       35,  71,  62,  77,  10,   5,  11,   6,  28,  40,  64,  48,  65,   2,  21,  43, 
       70,  12,   9,   2,   4,  24,  48,  64,  16,  49,  67,  38,  13,  11,   7,  14, 
       12,   8,  16,  32,  64,  16,  33,  66,  52,  73,  50,  53,  59,  55,)


def ktantan_one_round(state, key, round):
    output_a = state[LEN_L_2 + X[1]] ^ state[LEN_L_2 + X[2]] \
             ^ (state[LEN_L_2 + X[3]] * state[LEN_L_2+ X[4]]) ^ key[k_a[round]]
    if IR[round]:
        output_a ^= state[LEN_L_2 + X[5]]
    
    output_b = state[Y[1]] ^ state[Y[2]] ^ (state[Y[3]] * state[Y[4]]) \
             ^ (state[Y[5]] * state[Y[6]]) ^ key[k_b[round]]
    
    state[LEN_L_2] = output_b
    for i in range(LEN_L_1 + LEN_L_2 - 1, 0, -1):
        state[i] = state[i - 1]
    state[0] = output_a


def ktantan(state, key):
    for round in range(254):
        ktantan_one_round(state, key, round)
#        if LEN_L_1 + LEN_L_2 > 32:
#            ktantan_one_round(state, key, round)
#            if LEN_L_1 + LEN_L_2 > 48:
#                ktantan_one_round(state, key, round)


if __name__ == '__main__':
    import sys
    text = [0] * 64
    key = [1] * 80
    ktantan(text, key)
    for i in range(31, 0, -1):
        sys.stdout.write(str(text[i]))
    print
    
        
